from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import pdfplumber
import chromadb
import re
import os

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def test():
    return "hello"

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    global collection
    pdf_file = request.files.get('pdf_file')    # 獲取上傳的 PDF 檔案
    if not pdf_file:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file_path = os.path.join('upload', pdf_file.filename)
    if not os.path.exists('upload'):
        os.makedirs('upload')
    pdf_file.save(file_path)

    # 读取 PDF 文件并提取文本
    pdf_text = extract_text_from_pdf(file_path)
    splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=20)
    chunks = splitter.split_text(pdf_text)

    # 生成嵌入并保存到 Chroma
    embeddings = embeddings_model.encode(chunks)
    collection = add_embedding_to_chroma(embeddings, chunks)

    # 返回 JSON 响应
    return jsonify({'message': 'PDF uploaded and processed successfully'}), 200



@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input')  # 獲取使用者輸入

    if not user_input:
        return jsonify({'response': '未提供使用者輸入。'})

    try:
        # 根據使用者輸入進行查詢
        results = collection.query(query_texts=[user_input], n_results=2)

        # 檢查查詢結果並生成 AI 回應
        if results and 'documents' in results and len(results['documents']) > 0:
            document = results['documents'][0][0]  # 根據實際結果格式進行調整
            query = f"使用者提問: {user_input}\n根據以下內容回答問題：{document}"
            response = TAIDEchat(query)
            return jsonify({'response': response})

        return jsonify({'response': "未找到相關資訊。"})
        
    
    except Exception as e:
        # 打印錯誤訊息便於除錯
        print(f"處理 PDF 時發生錯誤: {str(e)}")
        return jsonify({'error': str(e)}), 500


# 用 TAIDE 模型生成回應
def TAIDEchat(sInput):
    device = "cuda"  # 如果你使用的是 CUDA，加速推理

    messages = [
        {"role": "system", "content": "你是一位助手"},
        {"role": "user", "content": sInput}
    ]

    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    generated_ids = model.generate(
        model_inputs.input_ids,
        attention_mask=model_inputs['attention_mask'],
        max_new_tokens=256,
        pad_token_id=tokenizer.eos_token_id
    )

    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    print(response)
    
    return response

# PDF 提取文本
def extract_text_from_pdf(pdf_data):
    text = ""
    with pdfplumber.open(pdf_data) as pdf:
        for page in pdf.pages:
            text += page.extract_text(x_tolerance=1, y_tolerance=1)
    
    # 清理空格、換行
    text = re.sub(r'\s+', ' ', text)
    return text

# 初始化 LLM 模型
model = AutoModelForCausalLM.from_pretrained("taide/TAIDE-LX-7B-Chat", load_in_4bit=True)
tokenizer = AutoTokenizer.from_pretrained("taide/TAIDE-LX-7B-Chat", use_fast=False)

# 初始化嵌入模型
embeddings_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

# 添加嵌入到 Chroma DB
def add_embedding_to_chroma(embeddings, chunks):
    # 連接到 Chroma DB
    db_path = os.path.join("..", "Embedding_DB.db") # 請根據實際路徑進行調整
    chroma_client = chromadb.PersistentClient(path=db_path)
    print('Connected to Chroma')

    try:
        # 檢查 collection 是否已存在
        collection = chroma_client.get_collection(name="collection")
        print("Collection already exists, using the existing one.")
    except ValueError:
        # 如果 collection 不存在，則創建一個新的 collection
        collection = chroma_client.create_collection(
            name="collection",
            embedding_function=embeddings_model,
            metadata={"hnsw:space": "cosine"}
        )
        print("Created a new collection.")

    # 檢查 collection 中已有的文檔
    try:
        existing_docs = collection.get(include=['documents'])
        existing_docs_text = existing_docs['documents'] if 'documents' in existing_docs else []
        print(f"Existing documents count: {len(existing_docs_text)}")
    except Exception as e:
        print(f"Error fetching existing documents: {str(e)}")
        existing_docs_text = []

    new_chunks = []
    new_embeddings = []
    new_ids = []

    for i, chunk in enumerate(chunks):
        if chunk not in existing_docs_text:
            new_chunks.append(chunk)
            new_embeddings.append(embeddings[i].tolist())  # 將嵌入轉換為列表
            new_ids.append(f'id{i+1+len(existing_docs_text)}')  # 生成新的 ID

    if new_chunks:
        collection.add(
            documents=new_chunks,
            embeddings=new_embeddings,
            ids=new_ids
        )
        print('New embeddings added to the collection')
    else:
        print('No new embeddings to add')

    return collection



if __name__ == '__main__':
    app.run(port=5000)
