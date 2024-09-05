from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
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

@app.route('/process_pdf', methods=['POST'])
def process_pdf():
    user_input = request.form.get('user_input')  # 獲取使用者輸入
    pdf_file = request.files.get('pdf_file')    # 獲取上傳的 PDF 檔案

    file_path = os.path.join('upload', pdf_file.filename)
    pdf_file.save(file_path)

    if not pdf_file or not user_input:
        return jsonify({'response': '未提供 PDF 檔案或使用者輸入。'})

    try:
        # 讀取 PDF 檔案
        pdf_text = extract_text_from_pdf(file_path)
        # 分割文字成塊
        splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=20)
        chunks = splitter.split_text(pdf_text)

        # 生成嵌入向量
        embeddings = embeddings_model.encode(chunks)

        # 將嵌入向量添加到 Chroma DB
        collection = add_embedding_to_chroma(embeddings, chunks)

        # 根據使用者輸入進行查詢
        results = collection.query(query_texts=[user_input], n_results=3)

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


# 调用 TAIDE 模型生成响应
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
        max_new_tokens=512,
        pad_token_id=tokenizer.eos_token_id
    )

    # 去除输入部分，只保留生成的响应
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    print(response)
    
    return response

# 从 PDF 提取文本
def extract_text_from_pdf(pdf_data):
    text = ""
    with pdfplumber.open(pdf_data) as pdf:
        for page in pdf.pages:
            text += page.extract_text(x_tolerance=1, y_tolerance=1)
    
    # 清理空格、换行符等
    text = re.sub(r'\s+', ' ', text)
    return text

# 初始化 LLM 模型
model = AutoModelForCausalLM.from_pretrained("taide/TAIDE-LX-7B-Chat", load_in_4bit=True)
tokenizer = AutoTokenizer.from_pretrained("taide/TAIDE-LX-7B-Chat", use_fast=False)

# 初始化嵌入模型
embeddings_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

# 添加嵌入到 Chroma 数据库
def add_embedding_to_chroma(embeddings, chunks):
    # 连接到 Chroma 数据库
    chroma_client = chromadb.PersistentClient(path=r"C:\Users\USER\Desktop\llm\Embedding_DB.db")
    print('Connected to Chroma')

    try:
        # 尝试获取现有的 collection
        collection = chroma_client.get_collection(name="collection")
        print("Collection already exists, using the existing one.")
    except ValueError:
        # 如果 collection 不存在，则创建新的 collection
        collection = chroma_client.create_collection(
            name="collection",
            embedding_function=embeddings_model,
            metadata={"hnsw:space": "cosine"}
        )
        print("Created a new collection.")

    # 获取已存在的嵌入文档的内容
    try:
        existing_docs = collection.get(include=['documents'])
        existing_docs_text = existing_docs['documents'] if 'documents' in existing_docs else []
        print(f"Existing documents count: {len(existing_docs_text)}")
    except Exception as e:
        print(f"Error fetching existing documents: {str(e)}")
        existing_docs_text = []

    # 准备存储新的嵌入
    new_chunks = []
    new_embeddings = []
    new_ids = []

    for i, chunk in enumerate(chunks):
        # 如果 chunk 文本不存在于现有文档中，则添加
        if chunk not in existing_docs_text:
            new_chunks.append(chunk)
            new_embeddings.append(embeddings[i].tolist())  # 将 numpy.ndarray 转换为 list
            new_ids.append(f'id{i+1+len(existing_docs_text)}')  # 保证 id 是唯一的

    # 添加新数据到 collection 中
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
