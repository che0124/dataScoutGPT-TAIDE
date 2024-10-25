---
{}
---
* [中文版](./README.md)

# Introduction
* The [TAIDE project](https://taide.tw/index) aims to develop a generative AI dialogue engine model that is tailored to the linguistic and cultural characteristics of Taiwan, while also establishing a trustworthy AI environment. By combining academic, industrial, and research resources, the project seeks to advance the development of trustworthy generative AI, enhancing Taiwan's international competitiveness, promoting industrial development, and reducing dependence on foreign technologies.
* The large language models developed in this project are based on Meta's [LLaMA2-7b](https://huggingface.co/meta-llama/Llama-2-7b-hf) release, incorporating text and training materials from various fields in Taiwan to enhance the model's ability to respond in Traditional Chinese and perform well in specific tasks. The publicly released models are as follows:
    * [TAIDE-LX-7B](https://huggingface.co/taide/TAIDE-LX-7B): This model is a continuous pretrained version with Traditional Chinese data based on LLaMA2-7b. It is suitable for scenarios where users intend to further fine-tune the model. Since the pre-trained model has not undergone fine-tuning and preference alignment, it may produce malicious or unsafe outputs. Please use with caution.
    * [TAIDE-LX-7B-Chat](https://huggingface.co/taide/TAIDE-LX-7B-Chat): This model enhances office-related tasks and multi-turn question-and-answer dialogue capabilities through instruction tuning based on TAIDE-LX-7B. It is suitable for scenarios such as chat conversations or task assistance. TAIDE-LX-7B-Chat also provides a [4-bit quantization model](https://huggingface.co/taide/TAIDE-LX-7B-Chat-4bit). The quantization model is primarily offered for user convenience but may affect performance and introduce unforeseen issues. Users are advised to understand and take note of this.

# Model Parameters
* Parameters: 7B
* Max context length: 4K
* Training token in Traditional Chinese: 41.44B
* Training time: 1531.82 H100 GPU Hours

# Features
* Expanding the character and word count by 24,720 to enhance the model's ability to process Traditional Chinese.
* Strictly vetting training data for the model to improve its trustworthiness and applicability.
* Enhancing the model's performance for tasks such as summarization, writing articles, writing letters, and translating between Chinese and English, which are commonly used in office settings.
* Strengthening the model's understanding of Taiwan-specific culture, terminology, and context.
* Equip the model with multi-turn conversation capabilities.

# Examples
| Task | User input | Model output |
| --- | -------- | ------- |
| Writing articles | 請以以下內容為基礎，寫一篇文章：撰寫一篇作文，題目為《一張舊照片》，內容要求為：選擇一張令你印象深刻的照片，說明令你印象深刻的原因，並描述照片中的影像及背後的故事。記錄成長的過程、與他人的情景、環境變遷和美麗的景色。 | 以下是根據指令創作的一篇作文：<br><br>《一張舊照片》<br><br>在我塵封已久的家族相簿中，有一張特別吸引我的舊照片，那張照片記錄了我們家族成員在過往美好時光的歡聚，至今仍舊令人回味無窮。這張照片是我奶奶在二十多年前舉辦的一場家族聚會上所拍下的，照片中的人物包括了我的父母、祖父母、叔叔、姑姑和表哥等，大家臉上洋溢著幸福的笑容，彷彿時光靜止般地美好。<br><br>照片中的場景十分溫馨，大家圍坐在一張長方形的餐桌上，桌上擺滿了美味的食物和飲料。桌上的菜餚是傳統中式的佳餚，有香噴噴的烤全魚、嫩滑的雞肉和鮮甜的蔬菜，這些菜餚是當年奶奶親自烹調的，她手藝精湛，讓每個人都吃得津津有味。<br><br>最讓我印象深刻的是，照片中還拍到了我年幼時的模樣。我坐在桌子的另一端，手裡拿著一碗湯，臉上帶著滿足的笑容。那時的我才剛滿周歲，對於這場盛大的家族聚會還感到十分新奇。從這張照片中，我能感受到當年家族成員間的親密和溫暖，即使過了這麼多年，那份情感卻依然牢固地存在著。<br><br>這張照片背後有著動人的故事。在那個時代，我的祖父母和父母都還在讀中學，他們每天都會放學後到農田裡幫忙，辛勤地耕作以維持一家人的生計。儘管生活條件並不富裕，但他們仍舊保持著樂觀的態度和對生活的熱愛。每年到了秋天，只要收獲季節來臨，他們就會舉辦家族聚會，邀請所有親戚朋友前來共享豐收的喜悅。<br><br>隨著歲月的流逝，我逐漸長大，開始工作和生活。每次回鄉，我都會抽空去探望老人家，聽聽他們當年的往事，感受那段刻骨銘心的時光。而這張舊照片，也將一直陪伴著我，成為我珍貴回憶的一部分。它見證了我們的成長和變遷，也記錄下了那些難以忘懷的美好時刻。<br><br>這張照片不僅展示了家族的親情和溫暖，還折射出那個時代人們勤勞樸實的生活方式和對傳統的尊重。如今，隨著社會的快速發展，許多傳統的美德和風俗正在逐漸消失。我們應該好好珍惜這樣的回憶和文化，將它們傳承下去，讓後代子孫也能感受到那份來自歷史的溫情和傳承。<br><br>因此，我決定將這張照片好好保管起來，並常常拿出來看。它不僅是一張舊照片，更是一段寶貴的回憶和家族精神的象徵。我希望未來能有機會重現當年的盛況，再一次聚在一起，分享彼此的生活和故事，讓那份親情和友情繼續在時光中蔓延，永不消逝。 |
| Writing letters   | 請以品牌經理的身份，給廣告公司的創意總監寫一封信，提出對於新產品廣告宣傳活動的創意建議。 | 尊敬的創意總監：<br><br>我寫這封信是為了向您提出一些關於我們新產品廣告宣傳活動的創意建議。我們公司即將推出一款全新的產品，為了確保它在市場上取得成功，我們希望透過一個引人注目的廣告宣傳活動來吸引消費者的注意。<br><br>在考慮廣告的創意和策略時，有幾個因素需要納入考量。首先，我們要針對目標客群進行研究，以瞭解他們的需求和喜好。其次，我們要確保廣告內容具有吸引力和說服力，能引起目標客群的共鳴。最後，我們要利用各種媒體平臺和數位行銷工具，以擴大廣告的影響力。<br><br>基於這些因素，我提出以下幾點創意建議：<br><br>1. 產品定位：我們可將這款新產品定位為高端、環保、健康和時尚的代表，強調其獨有的功能和特色。在廣告中，我們可以透過生動的視覺效果和簡潔的語言來傳達這些特點。<br>2. 故事行銷：在廣告中講述一個與產品功能相關的動人故事，讓消費者能更深入地瞭解產品所帶來的生活變化。例如，我們可以講述一位忙碌的職業婦女，如何使用我們的新產品在工作和生活中取得平衡的故事。<br>3. 名人效應：邀請一位受歡迎的公眾人物或意見領袖擔任產品代言人，利用他們的影響力來推廣產品。這不僅可以增加產品曝光度，還能讓更多消費者信任和信賴產品。<br>4. 跨界合作：與一些相關產業（如時尚、環保、健康等）進行跨界合作，共同推出限量版或聯名產品。這種合作不僅能吸引不同領域的消費者，還能為產品帶來更多話題性和收藏價值。<br>5. 數位行銷：充分利用社群媒體、搜尋引擎和電郵行銷等數位工具，在整個廣告宣傳過程中保持一致性的訊息和形象。我們也可製作一系列短視頻和線上活動，以增加消費者參與度和品牌忠誠度。<br>6. 創新形式：嘗試使用新穎的廣告形式，如AR（擴增實境）、VR（虛擬實境）和360度影片等，給消費者帶來全新的廣告體驗。這種創新形式不僅能吸引消費者目光，還能提高產品在市場上的辨識度。<br>7. 活動參與：在廣告宣傳活動中加入互動環節，如產品試用、抽獎和優惠券等，鼓勵消費者積極參與並分享他們的體驗。這將有助於口碑傳播，進一步擴大產品影響力。<br><br>綜合以上建議，我希望我們能製定出一套全面而富有創意的廣告宣傳活動計劃，以最大限度地提升新產品在市場上的競爭力。如果您有任何疑問或需要進一步討論，歡迎隨時與我聯絡。謝謝您的關注和支援！<br><br>祝商祺！<br><br>您的品牌經理<br><br>（註：此信件可根據實際情況和產品特點進行調整） |
| Summarization   | 請將這篇文章精簡條理化:「產業創新條例第10條之2及第72條條文修正案」俗稱「台版晶片法」,針對半導體、電動車、5G等技術創新且居國際供應鏈關鍵地位公司,提供最高25%營所稅投抵優惠,企業適用要件包含當年度研發費用、研發密度達一定規模,且有效稅率達一定比率。<br>為因應經濟合作暨發展組織(OECD)國家最低稅負制調整,其中有效稅率門檻,民國112年訂為12%,113年料將提高至15%,但仍得審酌國際間最低稅負制實施情形。<br>經濟部官員表示,已和財政部協商進入最後階段,除企業研發密度訂在6%,目前已確認,企業購置先進製程的設備投資金額達100億元以上可抵減。<br>財政部官員表示,研商過程中,針對台灣產業與其在國際間類似的公司進行深入研究,在設備部分,畢竟適用產創10之2的業者是代表台灣隊打「國際盃」,投入金額不達100億元,可能也打不了。<br>至於備受關注的研發費用門檻,經濟部官員表示,歷經與財政部來回密切討論,研發費用門檻有望落在60億至70億元之間。<br>財政部官員指出,研發攸關台灣未來經濟成長動能,門檻不能「高不可攀」,起初雖設定在100億元,之所以會調降,正是盼讓企業覺得有辦法達得到門檻、進而適用租稅優惠,才有動力繼續投入研發,維持國際供應鏈關鍵地位。<br>經濟部官員表示,因廠商研發費用平均為30、40億元,其中,IC設計業者介於30億至60億元範圍,若將門檻訂在100億元,符合條件的業者較少、刺激誘因不足;此外,若符合申請門檻的業者增加,將可提高企業在台投資金額,財政部稅收也能因此獲得挹注。<br>IC設計業者近日頻頻針對產創10之2發聲,希望降低適用門檻,加上各國力拚供應鏈自主化、加碼補助半導體產業,經濟部官員表示,經濟部和財政部就產創10之2達成共識,爭取讓更多業者受惠,盼增強企業投資力道及鞏固台灣技術地位。<br>財政部官員表示,租稅獎勵的制定必須「有為有守」,並以達到獎勵設置目的為最高原則,現階段在打「國內盃」的企業仍可適用產創第10條、10之1的租稅優惠,共同壯大台灣經濟發展。<br>經濟部和財政部正就研發費用門檻做最後確認,待今明兩天預告子法之後,約有30天時間,可與業界進一步討論及調整,盼產創10之2能在6月上路。 |  台灣「產業創新條例」的修正案，又稱「台版晶片法」,旨在支持半導體、電動車及5G技術領先企業的創新。新政策提供最高25%的所得稅抵免，企業需滿足當年度研發費用達一定規模、研發密度超過6%以及有效稅率達一定比率等條件。因應國際間對企業最低稅負制度的調整，台灣的門檻預計分別於2023年和2024年達到12%和15%。目前，與財政部討論後，確定100億元的設備投資抵免是可行的誘因，且研發費用門檻預計會在60至70億元之間。對於降低門檻的要求，經濟部和財政部已達成共識，旨在擴大受惠範圍並鼓勵企業投資以維持供應鏈的關鍵地位。此外，針對IC設計業者的訴求，也考慮調降門檻。預計此法案將在近期內實施，相關討論和調整將在預告期後進一步進行。  |
| Translation   | 以下提供英文內容，請幫我翻譯成中文。Dongshan coffee is famous for its unique position, and the constant refinement of production methods. The flavor is admired by many caffeine afficionados. | 東山咖啡以得天獨厚的地位，不斷精研的製作工藝著稱，風味獲諸多咖啡愛好者推崇。 |

# Usage
* Sample code
    * The sample code and documentation will be released on GitHub later.
* tokenizer should set to slow mode
    ```python
    tokenizer = AutoTokenizer.from_pretrained("taide/TAIDE-LX-7B-Chat", use_fast=False)
    ```
* Prompt template
    * Normal QA
        ```python
        f"<s>[INST] {question} [/INST]"
        ```
        * Replace {question} with user input
    * QA with system prompt
        ```python
        f"<s>[INST] <<SYS>>\n{sys}\n<</SYS>>\n\n{question} [/INST]"
        ```
        * Replace {sys} with system prompt，ex：你是一個來自台灣的AI助理，你的名字是 TAIDE，樂於以台灣人的立場幫助使用者，會用繁體中文回答問題。
        * Replace {question} as user input
    * Multi turns conversation
        ```python
        f"<s>[INST] <<SYS>>\n{sys}\n<</SYS>>\n\n{question1} [/INST] {model_answer_1} </s><s>[INST] {question2} [/INST]"
        ```
        * Replace {sys} with system prompt
        * Replace {question1} with user input 1
        * Replace {model_anwer_1} with model response 1
        * Replace {question2} with user input 2
* Huggingface Chat Template
    * Normal QA
        ```python
        chat = [
            {"role": "user", "content": "{question}"},
        ]
        prompt = tokenizer.apply_chat_template(chat)
        ```
        * Replace {question} with user input
    * QA with system prompt
        ```python
        chat = [
            {"role": "system", "content": "{sys}"},
            {"role": "user", "content": "{question}"},
        ]
        prompt = tokenizer.apply_chat_template(chat)
        ```
        * Replace {sys} with system prompt，ex：你是一個來自台灣的AI助理，你的名字是 TAIDE，樂於以台灣人的立場幫助使用者，會用繁體中文回答問題。
        * Replace {question} as user input
    * Multi turns conversation
        ```python
        chat = [
            {"role": "system", "content": "{sys}"},
            {"role": "user", "content": "{question1}"},
            {"role": "assistant", "content": "{model_anwer_1}"},
            {"role": "user", "content": "{question2}"},
        ]
        prompt = tokenizer.apply_chat_template(chat)
        ```
        * Replace {sys} with system prompt
        * Replace {question1} with user input 1
        * Replace {model_anwer_1} with model response 1
        * Replace {question2} with user input 2

# Training methods
* Software / hardware spec
    * GPU: H100
    * Training Framework: PyTorch
* Data preprocessing
    * Character normalization
    * Deduplication
    * Denoise
        * Html tag、javascript in web content
        * Non-standard characters or garbage characters
        * Posts with an insufficient number of characters
        * Removing specific formats such as extra line breaks added for formatting purposes
    * Removing personal information such as emails and phone numbers.
    * Remove inappropriate content such as gambling, pornography, etc..
* Character and word expanding
    * Enhancing the performance of Traditional Chinese input and output, the expanded data include the following two parts:
        * Obtaining Chinese characters from the Ministry of Education's ["Variant Chinese Characters Dictionary" and "Corrected Characters Table"](https://dict.variants.moe.edu.tw/appendix.jsp?ID=1&ID=0).
        * Collecting over 5,000,000 sentences with more than 100 characters each from the Traditional Chinese Wikipedia, news articles, and the Chinese Common Crawl data (2.1G), used to train the tokenizer for Chinese characters and words.
* Continuous pretraining (CP)
    * Supplementing the model with a large amount of reliable Traditional Chinese knowledge.
    * Hyper parameters
        * optimizer: AdamW
        * learning rate: 1e-4
        * batch size: 1M tokens
        * epoch: 1
* Fine tune (FT)
    * Enabling the model to answer questions in Traditional Chinese.
    * Hyper parameters
        * optimizer: AdamW
        * learning rate: 5e-5
        * batch size: 256K tokens
        * epoch: 3

# Training Data
* Continuous pre-training data (about 140GB)
| Dataset | Description |
| --- | -------- |
| Litigation Data | [Civil litigation data](https://judgment.judicial.gov.tw/FJUD/default.aspx) from various levels of courts in the judicial rulings, including data from 2013/01 to 2023/12. |
| CNA news | The [CNA news](https://www.cna.com.tw/) includes daily news articles from June 1993 to June 2023, spanning a period of 30 years. The content covers various domains such as domestic and international politics, society, economy, culture, education, and lifestyle. |
| ETtoday news | [ETtoday news](https://www.ettoday.net/) data, including data from 2011/10 to 2023/12. |
| Legislative Yuan Gazette | The [Legislative Yuan Gazette](https://ppg.ly.gov.tw/ppg/) contains data from the 1st session of the 8th term to the 7th session of the 10th term. |
| Publisher Website Book Introduction | Includes book introduction data from the websites of [SunColor](https://www.suncolor.com.tw/), [Gotop](https://www.gotop.com.tw/) publishers. |
| Abstracts of GRB research projects | [GRB](https://www.grb.gov.tw/) is an information system that compiles research projects funded by government grants and their outcome reports. This dataset primarily includes research project abstracts from 1993 to 2023, including both Chinese and their English counterparts. |
| Academic conference proceedings abstracts | The [database](https://sticnet.stpi.narl.org.tw/sticloc/ttscalle?meet:) contains academic conference proceedings held in Taiwan from 1988 to 2009. |
| Taiwan Panorama magazine | [Taiwan Panorama magazine](https://www.taiwan-panorama.com/) contains articles from July 1993 to June 2023, spanning 30 years. The content focuses on Taiwanese culture, tourism, and local customs. |
| 樂詞網 | 《[樂詞網](https://terms.naer.edu.tw/)》covers approximately 187,000 academic terms in the humanities and social sciences, along with their translations. |
| Data from various ministries and commissions | Including partial data from government department websites such as the Executive Yuan's "[National Overview](https://www.ey.gov.tw/state/)", the Ministry of Culture's "[National Cultural Memory Bank](https://memory.culture.tw/)", the National Development Council's "[Archives Support Teaching Network](https://art.archives.gov.tw/index.aspx)", the Ministry of Transportation's "[Traffic Safety Portal](https://168.motc.gov.tw/)", etc. |
| Business Today | [Business Today](https://www.businesstoday.com.tw/) Magazine is a weekly magazine focused on finance. The dataset includes articles from 2008/01 to 2023/07. |
| Mandarin and idiom dictionary from the Ministry of Education | Dataset including:<br>[Idiom Dictionary](https://dict.idioms.moe.edu.tw/search.jsp?webMd=1&la=0): Contains 5,338 idioms, including definitions, original stories, usage explanations, and example sentences.<br>[Revised Mandarin Dictionary](https://dict.revised.moe.edu.tw/?la=0&powerMode=0): contains Chinese words and various vocabulary, including pronunciation, radicals, definitions, and other information, totaling approximately 165,539 entries.<br>[Concise Mandarin Dictionary](https://dict.concised.moe.edu.tw/?la=0&powerMode=0): is a condensed version of the "Revised Mandarin Dictionary", containing a total of 45,247 entries. |
| SCITechVista | The dataset includes science news and popular science articles from the [SCITechVista](https://scitechvista.nat.gov.tw/) website. |
| iKnow | The [iKnow](https://iknow.stpi.narl.org.tw/) platform provides information on market trends, strategic analysis, patent knowledge, and technology transaction information for Taiwan and the global technology industry. The dataset includes data from 2005/01 to 2023/07. |
| Science Development Monthly Magazine | [Science Development Monthly Magazine](https://ejournal.stpi.narl.org.tw/sd) is a popular science publication published by the National Science Council (NSC) to promote science education. It includes articles from 2004/10 to 2020/12. In 2021, the magazine was relaunched as "[CharmingSCITech](https://www.charmingscitech.nat.gov.tw/)" quarterly, providing new knowledge on international technology issues. |
| Legislation Database | The [Legislation Database](https://law.moj.gov.tw/) includes the latest central regulations, rules, draft bills, and local regulations issued by government agencies as of 2023/10. |
| Local Government Tourism Websites | Covering partial data from tourism websites of local government counties and cities in Taiwan. |
| Curriculum Guidelines from the National Institute of Education | The dataset includes curriculum guidelines for different subjects at various levels of education. |
| CNA's English and Chinese Name Translation Database | The English and Chinese Name Translation Database of the Central News Agency (CNA) collects translations of foreign and Chinese surnames, personal names, organizations, and place names used in news. |
| Fairy tales | A total of 20 fairy tale books, including "Tom Sawyer," "Peter Pan," "Alice's Adventures in Wonderland," "Uncle Long Legs," and more. |
| RedPajama-Data-V2 | Extracting English data from the [RedPajama-Data-v2](https://github.com/togethercomputer/RedPajama-Data) multilingual dataset |
| MathPile-commercial | A mathematics-focused dataset obtained from [MathPile-commercial](https://huggingface.co/datasets/GAIR/MathPile_Commercial) |
| Traditional Chinese Wikipedia Articles | The content of all articles in [Traditional Chinese Wikipedia](https://zh.wikipedia.org/zh-tw/%E4%B8%AD%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91), up to January 2023. |
| github-code-clean | An open-source code dataset on GitHub. After removing unlicensed code and documents. |
* Fine tune data
    * The TAIDE team trains the LLaMA2 series models to generate fine-tuning data, which generates single or multi-turn conversations on topics such as world knowledge, creative writing, general knowledge, translation, summarization, programming, and Taiwanese values. The fine tune data consists of 128K prompt-response pairs and will be released publicly later.

# Evaluation
* taide-bench
    * Data
        * Tasks include writing articles, writing letters, summarizing articles, translating from English to Traditional Chinese, translating from Traditional Chinese to English. There are 500 questions in total.
        * data link: [taide-bench](https://huggingface.co/datasets/taide/taide-bench)
    * Evaluation method
        * LLM as a Judge by GPT4
        * code link: [taide-bench-eval](https://github.com/taide-taiwan/taide-bench-eval)
    * Scores
| Model | Translating from Traditional Chinese to English | Translating from English to Traditional Chinese | Summerization | Writing articles | Writing letters | Average |
| --- | ----- | ----- | ---- | ---- | ---- | --- |
| TAIDE-LX-7B-Chat | 7.165 | 7.685 | 7.720 | 9.635 | 9.110 | 8.263 |
| GPT3.5 | 8.880 | 8.810 | 7.450 | 9.490 | 8.750 | 8.676 |
| LLAMA2 7B | 6.075 | 4.475 | 5.905 | 2.625 | 3.040 | 4.424 |
| LLAMA2 13B | 6.480 | 6.135 | 6.110 | 2.565 | 3.000 | 4.858 |
| LLAMA2 70B | 6.975 | 6.375 | 6.795 | 2.625 | 2.990 | 5.152 |

# License
* [TAIDE L Models Community License Agreement](https://drive.google.com/file/d/1FcUZjbUH6jr4xoCyAronN_slLgcdhEUd/view)

# Disclaimer
* Due to limitations in its design architecture and the inevitable biases in data, any response from the LLM model does not represent the stance of TAIDE. Additional security measures should be implemented before use, and responses may also contain incorrect information. Users are advised not to fully trust the responses.

# Development Team
* [https://taide.tw/index/teamList](https://taide.tw/index/teamList)

# Useful links
* [TAIDE official website](https://taide.tw/index)
* [TAIDE Huggingface](https://huggingface.co/taide)
* [TAIDE Github](https://github.com/taide-taiwan)
* [Kuwa AI](https://kuwaai.org/)

# Citation
* [TAIDE official website](https://taide.tw/index)
