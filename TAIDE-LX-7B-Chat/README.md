<<<<<<< HEAD
---
license: other
license_name: taide-l-models-community-license-agreement
license_link: https://drive.google.com/file/d/1FcUZjbUH6jr4xoCyAronN_slLgcdhEUd/view
extra_gated_heading: 您需要先同意授權條款才能使用此模型
extra_gated_fields:
  姓名(Name): text
  生日(Date of birth): date_picker
  國家(Country): country
  所屬單位(Affiliation): text
  geo: ip_location
  按下送出表示您同意社群授權同意書與個人資料蒐集告知聲明(By clicking Submit below I accept the terms of the license and privacy policy): checkbox

extra_gated_prompt: >-
  * ### [TAIDE L 類模型社群授權同意書(License)](https://drive.google.com/file/d/1FcUZjbUH6jr4xoCyAronN_slLgcdhEUd/view)
  
  * ### [個人資料蒐集告知聲明(Privacy policy)](https://drive.google.com/file/d/1JTfZu_MdU_TR1-1sn2jbQyW7TLrxjwS5/view)
  
extra_gated_button_content: 送出(Submit)
---
* [English Version](./README_en.md)

# 模型簡介
* [TAIDE計畫](https://taide.tw/index)致力於開發符合台灣語言和文化特性的生成式人工智慧對話引擎模型，同時建構可信任的人工智慧環境。結合產學研能量，推動可信任生成式人工智慧的發展，提升台灣在國際競爭中的地位，促進產業發展，避免對外國技術的依賴。
* 本計畫開發的大型語言模型以 Meta 公司釋出的 [LLaMA2-7b](https://huggingface.co/meta-llama/Llama-2-7b-hf) 為基礎，導入台灣不同領域可用的文本與訓練素材，提高模型在正體中文回應的能力與特定任務的表現。公開釋出的模型如下:
    * [TAIDE-LX-7B](https://huggingface.co/taide/TAIDE-LX-7B): 以 LLaMA2-7b 為基礎，僅使用繁體中文資料預訓練 (continuous pretraining)的模型，適合使用者會對模型進一步微調(fine tune)的使用情境。因預訓練模型沒有經過微調和偏好對齊，可能會產生惡意或不安全的輸出，使用時請小心。
    * [TAIDE-LX-7B-Chat](https://huggingface.co/taide/TAIDE-LX-7B-Chat): 以 TAIDE-LX-7B 為基礎，透過指令微調(instruction tuning)強化辦公室常用任務和多輪問答對話能力，適合聊天對話或任務協助的使用情境。TAIDE-LX-7B-Chat另外有提供[4 bit 量化模型](https://huggingface.co/taide/TAIDE-LX-7B-Chat-4bit)，量化模型主要是提供使用者的便利性，可能會影響效能與更多不可預期的問題，還請使用者理解與注意。

# 模型參數
* 參數量: 7B
* 最大內容長度 (context length): 4K
* 繁中訓練資料 token 量: 41.44B
* 訓練時間: 1531.82 H100 GPU Hours

# 特色
* 額外擴充24720個中文字元、字詞，強化模型處理繁體中文的能力
* 嚴格把關模型的訓練資料，提升模型生成資料的可信任性和適用性
* 針對自動摘要、寫信、寫文章、中翻英、英翻中等辦公室常用任務做加強
* 針對台灣在地文化、用語、國情等知識做加強
* 具備多輪問答對話能力

# 應用範例
| 任務 | 使用者輸入 | 模型輸出 |
| --- | -------- | ------- |
| 寫文章 | 請以以下內容為基礎，寫一篇文章：撰寫一篇作文，題目為《一張舊照片》，內容要求為：選擇一張令你印象深刻的照片，說明令你印象深刻的原因，並描述照片中的影像及背後的故事。記錄成長的過程、與他人的情景、環境變遷和美麗的景色。 | 以下是根據指令創作的一篇作文：<br><br>《一張舊照片》<br><br>在我塵封已久的家族相簿中，有一張特別吸引我的舊照片，那張照片記錄了我們家族成員在過往美好時光的歡聚，至今仍舊令人回味無窮。這張照片是我奶奶在二十多年前舉辦的一場家族聚會上所拍下的，照片中的人物包括了我的父母、祖父母、叔叔、姑姑和表哥等，大家臉上洋溢著幸福的笑容，彷彿時光靜止般地美好。<br><br>照片中的場景十分溫馨，大家圍坐在一張長方形的餐桌上，桌上擺滿了美味的食物和飲料。桌上的菜餚是傳統中式的佳餚，有香噴噴的烤全魚、嫩滑的雞肉和鮮甜的蔬菜，這些菜餚是當年奶奶親自烹調的，她手藝精湛，讓每個人都吃得津津有味。<br><br>最讓我印象深刻的是，照片中還拍到了我年幼時的模樣。我坐在桌子的另一端，手裡拿著一碗湯，臉上帶著滿足的笑容。那時的我才剛滿周歲，對於這場盛大的家族聚會還感到十分新奇。從這張照片中，我能感受到當年家族成員間的親密和溫暖，即使過了這麼多年，那份情感卻依然牢固地存在著。<br><br>這張照片背後有著動人的故事。在那個時代，我的祖父母和父母都還在讀中學，他們每天都會放學後到農田裡幫忙，辛勤地耕作以維持一家人的生計。儘管生活條件並不富裕，但他們仍舊保持著樂觀的態度和對生活的熱愛。每年到了秋天，只要收獲季節來臨，他們就會舉辦家族聚會，邀請所有親戚朋友前來共享豐收的喜悅。<br><br>隨著歲月的流逝，我逐漸長大，開始工作和生活。每次回鄉，我都會抽空去探望老人家，聽聽他們當年的往事，感受那段刻骨銘心的時光。而這張舊照片，也將一直陪伴著我，成為我珍貴回憶的一部分。它見證了我們的成長和變遷，也記錄下了那些難以忘懷的美好時刻。<br><br>這張照片不僅展示了家族的親情和溫暖，還折射出那個時代人們勤勞樸實的生活方式和對傳統的尊重。如今，隨著社會的快速發展，許多傳統的美德和風俗正在逐漸消失。我們應該好好珍惜這樣的回憶和文化，將它們傳承下去，讓後代子孫也能感受到那份來自歷史的溫情和傳承。<br><br>因此，我決定將這張照片好好保管起來，並常常拿出來看。它不僅是一張舊照片，更是一段寶貴的回憶和家族精神的象徵。我希望未來能有機會重現當年的盛況，再一次聚在一起，分享彼此的生活和故事，讓那份親情和友情繼續在時光中蔓延，永不消逝。 |
| 寫信   | 請以品牌經理的身份，給廣告公司的創意總監寫一封信，提出對於新產品廣告宣傳活動的創意建議。 | 尊敬的創意總監：<br><br>我寫這封信是為了向您提出一些關於我們新產品廣告宣傳活動的創意建議。我們公司即將推出一款全新的產品，為了確保它在市場上取得成功，我們希望透過一個引人注目的廣告宣傳活動來吸引消費者的注意。<br><br>在考慮廣告的創意和策略時，有幾個因素需要納入考量。首先，我們要針對目標客群進行研究，以瞭解他們的需求和喜好。其次，我們要確保廣告內容具有吸引力和說服力，能引起目標客群的共鳴。最後，我們要利用各種媒體平臺和數位行銷工具，以擴大廣告的影響力。<br><br>基於這些因素，我提出以下幾點創意建議：<br><br>1. 產品定位：我們可將這款新產品定位為高端、環保、健康和時尚的代表，強調其獨有的功能和特色。在廣告中，我們可以透過生動的視覺效果和簡潔的語言來傳達這些特點。<br>2. 故事行銷：在廣告中講述一個與產品功能相關的動人故事，讓消費者能更深入地瞭解產品所帶來的生活變化。例如，我們可以講述一位忙碌的職業婦女，如何使用我們的新產品在工作和生活中取得平衡的故事。<br>3. 名人效應：邀請一位受歡迎的公眾人物或意見領袖擔任產品代言人，利用他們的影響力來推廣產品。這不僅可以增加產品曝光度，還能讓更多消費者信任和信賴產品。<br>4. 跨界合作：與一些相關產業（如時尚、環保、健康等）進行跨界合作，共同推出限量版或聯名產品。這種合作不僅能吸引不同領域的消費者，還能為產品帶來更多話題性和收藏價值。<br>5. 數位行銷：充分利用社群媒體、搜尋引擎和電郵行銷等數位工具，在整個廣告宣傳過程中保持一致性的訊息和形象。我們也可製作一系列短視頻和線上活動，以增加消費者參與度和品牌忠誠度。<br>6. 創新形式：嘗試使用新穎的廣告形式，如AR（擴增實境）、VR（虛擬實境）和360度影片等，給消費者帶來全新的廣告體驗。這種創新形式不僅能吸引消費者目光，還能提高產品在市場上的辨識度。<br>7. 活動參與：在廣告宣傳活動中加入互動環節，如產品試用、抽獎和優惠券等，鼓勵消費者積極參與並分享他們的體驗。這將有助於口碑傳播，進一步擴大產品影響力。<br><br>綜合以上建議，我希望我們能製定出一套全面而富有創意的廣告宣傳活動計劃，以最大限度地提升新產品在市場上的競爭力。如果您有任何疑問或需要進一步討論，歡迎隨時與我聯絡。謝謝您的關注和支援！<br><br>祝商祺！<br><br>您的品牌經理<br><br>（註：此信件可根據實際情況和產品特點進行調整） |
| 摘要   | 請將這篇文章精簡條理化:「產業創新條例第10條之2及第72條條文修正案」俗稱「台版晶片法」,針對半導體、電動車、5G等技術創新且居國際供應鏈關鍵地位公司,提供最高25%營所稅投抵優惠,企業適用要件包含當年度研發費用、研發密度達一定規模,且有效稅率達一定比率。<br>為因應經濟合作暨發展組織(OECD)國家最低稅負制調整,其中有效稅率門檻,民國112年訂為12%,113年料將提高至15%,但仍得審酌國際間最低稅負制實施情形。<br>經濟部官員表示,已和財政部協商進入最後階段,除企業研發密度訂在6%,目前已確認,企業購置先進製程的設備投資金額達100億元以上可抵減。<br>財政部官員表示,研商過程中,針對台灣產業與其在國際間類似的公司進行深入研究,在設備部分,畢竟適用產創10之2的業者是代表台灣隊打「國際盃」,投入金額不達100億元,可能也打不了。<br>至於備受關注的研發費用門檻,經濟部官員表示,歷經與財政部來回密切討論,研發費用門檻有望落在60億至70億元之間。<br>財政部官員指出,研發攸關台灣未來經濟成長動能,門檻不能「高不可攀」,起初雖設定在100億元,之所以會調降,正是盼讓企業覺得有辦法達得到門檻、進而適用租稅優惠,才有動力繼續投入研發,維持國際供應鏈關鍵地位。<br>經濟部官員表示,因廠商研發費用平均為30、40億元,其中,IC設計業者介於30億至60億元範圍,若將門檻訂在100億元,符合條件的業者較少、刺激誘因不足;此外,若符合申請門檻的業者增加,將可提高企業在台投資金額,財政部稅收也能因此獲得挹注。<br>IC設計業者近日頻頻針對產創10之2發聲,希望降低適用門檻,加上各國力拚供應鏈自主化、加碼補助半導體產業,經濟部官員表示,經濟部和財政部就產創10之2達成共識,爭取讓更多業者受惠,盼增強企業投資力道及鞏固台灣技術地位。<br>財政部官員表示,租稅獎勵的制定必須「有為有守」,並以達到獎勵設置目的為最高原則,現階段在打「國內盃」的企業仍可適用產創第10條、10之1的租稅優惠,共同壯大台灣經濟發展。<br>經濟部和財政部正就研發費用門檻做最後確認,待今明兩天預告子法之後,約有30天時間,可與業界進一步討論及調整,盼產創10之2能在6月上路。 |  台灣「產業創新條例」的修正案，又稱「台版晶片法」,旨在支持半導體、電動車及5G技術領先企業的創新。新政策提供最高25%的所得稅抵免，企業需滿足當年度研發費用達一定規模、研發密度超過6%以及有效稅率達一定比率等條件。因應國際間對企業最低稅負制度的調整，台灣的門檻預計分別於2023年和2024年達到12%和15%。目前，與財政部討論後，確定100億元的設備投資抵免是可行的誘因，且研發費用門檻預計會在60至70億元之間。對於降低門檻的要求，經濟部和財政部已達成共識，旨在擴大受惠範圍並鼓勵企業投資以維持供應鏈的關鍵地位。此外，針對IC設計業者的訴求，也考慮調降門檻。預計此法案將在近期內實施，相關討論和調整將在預告期後進一步進行。  |
| 翻譯   | 以下提供英文內容，請幫我翻譯成中文。Dongshan coffee is famous for its unique position, and the constant refinement of production methods. The flavor is admired by many caffeine afficionados. | 東山咖啡以得天獨厚的地位，不斷精研的製作工藝著稱，風味獲諸多咖啡愛好者推崇。 |

# 使用說明
* 範例程式
    * 範例程式與文件後續會釋出到github
* tokenizer 必須設成 slow mode
    ```python
    tokenizer = AutoTokenizer.from_pretrained("taide/TAIDE-LX-7B-Chat", use_fast=False)
    ```
* prompt 樣版
    * 一般問答用法
        ```python
        f"<s>[INST] {question} [/INST]"
        ```
        * 將 {question} 替換成使用者的輸入
    * 加入 system prompt 的用法
        ```python
        f"<s>[INST] <<SYS>>\n{sys}\n<</SYS>>\n\n{question} [/INST]"
        ```
        * 將 {sys} 替換成指令，例如：你是一個來自台灣的AI助理，你的名字是 TAIDE，樂於以台灣人的立場幫助使用者，會用繁體中文回答問題。
        * 將 {question} 替換成使用者的問題
    * 多輪問答用法
        ```python
        f"<s>[INST] <<SYS>>\n{sys}\n<</SYS>>\n\n{question1} [/INST] {model_answer_1} </s><s>[INST] {question2} [/INST]"
        ```
        * 將 {sys} 替換成指令
        * 將 {question1} 替換成使用者的問題1
        * 將 {model_anwer_1} 替換成模型的回答1
        * 將 {question2} 替換成使用者的問題2
* Huggingface Chat 樣板
    * 一般問答用法
        ```python
        chat = [
            {"role": "user", "content": "{question}"},
        ]
        prompt = tokenizer.apply_chat_template(chat)
        ```
        * 將 {question} 替換成使用者的輸入
    * 加入 system prompt 的用法
        ```python
        chat = [
            {"role": "system", "content": "{sys}"},
            {"role": "user", "content": "{question}"},
        ]
        prompt = tokenizer.apply_chat_template(chat)
        ```
        * 將 {sys} 替換成指令，例如：你是一個來自台灣的AI助理，你的名字是 TAIDE，樂於以台灣人的立場幫助使用者，會用繁體中文回答問題。
        * 將 {question} 替換成使用者的問題
    * 多輪問答用法
        ```python
        chat = [
            {"role": "system", "content": "{sys}"},
            {"role": "user", "content": "{question1}"},
            {"role": "assistant", "content": "{model_anwer_1}"},
            {"role": "user", "content": "{question2}"},
        ]
        prompt = tokenizer.apply_chat_template(chat)
        ```
        * 將 {sys} 替換成指令
        * 將 {question1} 替換成使用者的問題1
        * 將 {model_anwer_1} 替換成模型的回答1
        * 將 {question2} 替換成使用者的問題2

# 訓練方法
* 軟硬體規格
    * 國網中心 H100
    * 訓練框架: PyTorch
* 資料前處理
    * 字元標準化
    * 去除重覆
    * 去除雜訊
        * 網頁資料的html tag、javascript
        * 非標準字元或亂碼
        * 字數過短的文章
        * 去除文章中的特定格式，如為排版增加的換行
    * 去除個資，如email、電話
    * 去除不當文字，如賭博、色情等
* 擴充字元字詞
    * 強化繁體中文輸入、輸出的效能，擴充資料包含下列2部分
        * 從[教育部異體字字典正字表](https://dict.variants.moe.edu.tw/appendix.jsp?ID=1&ID=0)獲取中文字元
        * 從繁中維基百科、新聞、中文common crawl資料抽取 500 萬條超過 100 個字元的句子(2.1G)，訓練中文字詞的 tokenizer
* 持續預訓練 (continuous pretraining, CP)
    * 補充大量來源可信賴的繁體中文知識
    * 超參數 (hyper parameters)
        * optimizer: AdamW
        * learning rate: 1e-4
        * batch size: 1M tokens
        * epoch: 1
* 微調 (fine tune, FT)
    * 讓模型可針對繁體中文提問回答問題
    * 超參數 (hyper parameters)
        * optimizer: AdamW
        * learning rate: 5e-5
        * batch size: 256K tokens
        * epoch: 3

# 訓練資料
* 持續預訓練資料(資料量約為140G)
| 資料集 | 資料描述 |
| --- | -------- |
| 訴訟資料 | 《[司法院裁判書](https://judgment.judicial.gov.tw/FJUD/default.aspx)》自2013年1月至2023年12月各級法院民事、刑事、行政訴訟資料。 |
| 中央社 | 《[中央社中文新聞](https://www.cna.com.tw/)》資料集含中央社自1993年6月至2023年06月，共30年份之每日新聞文章。內容涵蓋國內外政治、社會、財經、文教、生活等領域。 |
| ETtoday 新聞雲 | 《[ETtoday新聞雲](https://www.ettoday.net/)》資料，包含自2011年10月至 2023年12月的資料。 |
| 立法院公報 | 《[立法院公報](https://ppg.ly.gov.tw/ppg/)》包含自第8屆第1會期至第10屆第7會期之公報資料。 |
| 出版商網站書籍介紹 | 包含[三采](https://www.suncolor.com.tw/)、[Gotop](https://www.gotop.com.tw/)出版商網站上的書籍簡介。 |
| GRB 研究計畫摘要 | [GRB](https://www.grb.gov.tw/)為收錄由政府經費補助之研究計畫及其成果報告的資訊系統，此資料集主要收錄 1993年至 2023年之研究計畫摘要以及研究報告摘要，含中文及其英文對照。 |
| 學術會議論文摘要 | 收錄《[學術會議論文摘要資料庫](https://sticnet.stpi.narl.org.tw/sticloc/ttscalle?meet:)》中自1988至2009年由台灣所舉辦之學術會議論文。 |
| 光華雜誌 | 《[台灣光華雜誌](https://www.taiwan-panorama.com/)》含自1993年7月至2023年6月的文章，共30年份。內容著重於我國文化、觀光與民情等。 |
| 樂詞網 | 《[樂詞網](https://terms.naer.edu.tw/)》涵蓋文理領域約187萬則學術名詞及其譯名對照。 |
| 各部會資料 | 包含行政院「[國情簡介](https://www.ey.gov.tw/state/)」、文化部「[國家文化記憶庫](https://memory.culture.tw/)」、國發會「[檔案支援教學網](https://art.archives.gov.tw/index.aspx)」、交通部「[交通安全入口網](https://168.motc.gov.tw/)」等部會網站資料之部分資料。 |
| 今周刊 | 《[今周刊](https://www.businesstoday.com.tw/)》為一以財經為主的週刊雜誌，此資料集涵蓋2008年1月至2023年7月的文章。 |
| 教育部國語辭典、成語辭典 | 包含以下三項資料:<br>[教育部《成語典》](https://dict.idioms.moe.edu.tw/search.jsp?webMd=1&la=0)，含5,338條成語，內容包含每條成語的釋義、典故原文及其白話說明、用法說明、例句等。<br>[教育部《重編國語辭典修訂本》](https://dict.revised.moe.edu.tw/?la=0&powerMode=0)，收錄中文單字及各類辭彙，包含讀音、部首、釋義等資訊，共約165,539筆資料。<br>[教育部《國語辭典簡編本》](https://dict.concised.moe.edu.tw/?la=0&powerMode=0)，為《重編國語辭典修訂本》的簡編版本，共45,247筆資料。 |
| 科技大觀園資料 | 含《[科技大觀園網站](https://scitechvista.nat.gov.tw/)》上的科學新知以及科普文章。 |
| iKnow 科技產業資訊室 | 《[科技產業資訊室](https://iknow.stpi.narl.org.tw/)（iKnow）》提供台灣及全球的科技市場趨勢、策略分析、專利知識，及技術交易資訊，專注於科技產業的創新與發展，包含自 2008 年至 2023 年。 |
| 科學發展月刊 | 《[科學發展月刊](https://ejournal.stpi.narl.org.tw/sd)》為國科會為推廣科學教育而出版的科普刊物，含自2004年10月至2020年12月之科普文章；2021年起，以《[科技魅癮](https://www.charmingscitech.nat.gov.tw/)》季刊重新出發，提供國際關注科技議題的新知文章。 |
| 法規資料庫 | 《[法規資料庫](https://law.moj.gov.tw/)》含截自 112 年 10 月各政府部門最新發布之中央法規、行政規則、法規命令草案及地方自治法規等。 |
| 各地政府旅遊網 | 涵蓋台灣部分縣市地方政府觀光旅遊網站上之部分資料。 |
| 國教院課程綱要(十二年國教) | 含十二年國教課程綱要之總綱以及各級學校不同科目之課程綱要。 |
| 中央社譯名檔資料庫 | 《中央社譯名檔資料庫》蒐集中央社新聞業務上翻譯過的中外姓氏、人名、組織、地名等譯名對照。 |
| 童話書 | 共 20 本童話書，含湯姆歷險記、小飛俠、愛麗絲夢遊仙境、長腿叔叔等。 |
| RedPajama-Data-V2 | 從國外開放多國語言語料庫 [RedPajama-Data-v2](https://github.com/togethercomputer/RedPajama-Data) 取出英文資料 |
| MathPile-commercial | 國外開放數學語料庫 [MathPile-commercial](https://huggingface.co/datasets/GAIR/MathPile_Commercial) |
| 中文維基百科 | 《[中文維基百科](https://zh.wikipedia.org/zh-tw/%E4%B8%AD%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91)》截至2023年1月所有條目的內容。 |
| github-code-clean | 為 github 開源程式碼資料集，去除unlicense的程式碼和文件。 |
* 微調資料
    * TAIDE團隊訓練llama2系列模型來產生微調資料資料，產生的任務包含世界知識、創意寫作、普通常識、翻譯、摘要、程式、台灣價值等單輪或多輪對話問答共 128K 筆。微調資料後續會對外釋出。

# 模型評測
* taide-bench
    * 評測資料
        * 寫文章、寫信、摘要、英翻中、中翻英，共500題
        * 資料連結: [taide-bench](https://huggingface.co/datasets/taide/taide-bench)
    * 評測方法
        * gpt4評分
        * 評分程式: [taide-bench-eval](https://github.com/taide-taiwan/taide-bench-eval)
    * 評測分數
| 模型 | 中翻英 | 英翻中 | 摘要 | 寫文章 | 寫信 | 平均 |
| --- | ----- | ----- | ---- | ---- | ---- | --- |
| TAIDE-LX-7B-Chat | 7.165 | 7.685 | 7.720 | 9.635 | 9.110 | 8.263 |
| GPT3.5 | 8.880 | 8.810 | 7.450 | 9.490 | 8.750 | 8.676 |
| LLAMA2 7B | 6.075 | 4.475 | 5.905 | 2.625 | 3.040 | 4.424 |
| LLAMA2 13B | 6.480 | 6.135 | 6.110 | 2.565 | 3.000 | 4.858 |
| LLAMA2 70B | 6.975 | 6.375 | 6.795 | 2.625 | 2.990 | 5.152 |

# 授權條款
* [TAIDE L 類模型社群授權同意書](https://drive.google.com/file/d/1FcUZjbUH6jr4xoCyAronN_slLgcdhEUd/view?usp=drive_link)

# 免責聲明
* LLM 模型由於設計架構的限制，以及資料難免有偏誤，語言模型的任何回應不代表 TAIDE 立場，使用前需要額外加入安全防護機制，且回應內容也可能包含不正確的資訊，使用者請勿盡信。

# 開發團隊
* [https://taide.tw/index/teamList](https://taide.tw/index/teamList)

# 相關連結
* [TAIDE官網](https://taide.tw/index)
* [TAIDE Huggingface](https://huggingface.co/taide)
* [TAIDE Github](https://github.com/taide-taiwan)
* [Kuwa AI](https://kuwaai.org/)

# Citation
* [TAIDE官網](https://taide.tw/index)
=======
---
license: other
license_name: taide-l-models-community-license-agreement
license_link: https://drive.google.com/file/d/1FcUZjbUH6jr4xoCyAronN_slLgcdhEUd/view
extra_gated_heading: 您需要先同意授權條款才能使用此模型
extra_gated_fields:
  姓名(Name): text
  生日(Date of birth): date_picker
  國家(Country): country
  所屬單位(Affiliation): text
  geo: ip_location
  按下送出表示您同意社群授權同意書與個人資料蒐集告知聲明(By clicking Submit below I accept the terms of the license and privacy policy): checkbox

extra_gated_prompt: >-
  * ### [TAIDE L 類模型社群授權同意書(License)](https://drive.google.com/file/d/1FcUZjbUH6jr4xoCyAronN_slLgcdhEUd/view)
  
  * ### [個人資料蒐集告知聲明(Privacy policy)](https://drive.google.com/file/d/1JTfZu_MdU_TR1-1sn2jbQyW7TLrxjwS5/view)
  
extra_gated_button_content: 送出(Submit)
---
* [English Version](./README_en.md)

# 模型簡介
* [TAIDE計畫](https://taide.tw/index)致力於開發符合台灣語言和文化特性的生成式人工智慧對話引擎模型，同時建構可信任的人工智慧環境。結合產學研能量，推動可信任生成式人工智慧的發展，提升台灣在國際競爭中的地位，促進產業發展，避免對外國技術的依賴。
* 本計畫開發的大型語言模型以 Meta 公司釋出的 [LLaMA2-7b](https://huggingface.co/meta-llama/Llama-2-7b-hf) 為基礎，導入台灣不同領域可用的文本與訓練素材，提高模型在正體中文回應的能力與特定任務的表現。公開釋出的模型如下:
    * [TAIDE-LX-7B](https://huggingface.co/taide/TAIDE-LX-7B): 以 LLaMA2-7b 為基礎，僅使用繁體中文資料預訓練 (continuous pretraining)的模型，適合使用者會對模型進一步微調(fine tune)的使用情境。因預訓練模型沒有經過微調和偏好對齊，可能會產生惡意或不安全的輸出，使用時請小心。
    * [TAIDE-LX-7B-Chat](https://huggingface.co/taide/TAIDE-LX-7B-Chat): 以 TAIDE-LX-7B 為基礎，透過指令微調(instruction tuning)強化辦公室常用任務和多輪問答對話能力，適合聊天對話或任務協助的使用情境。TAIDE-LX-7B-Chat另外有提供[4 bit 量化模型](https://huggingface.co/taide/TAIDE-LX-7B-Chat-4bit)，量化模型主要是提供使用者的便利性，可能會影響效能與更多不可預期的問題，還請使用者理解與注意。

# 模型參數
* 參數量: 7B
* 最大內容長度 (context length): 4K
* 繁中訓練資料 token 量: 41.44B
* 訓練時間: 1531.82 H100 GPU Hours

# 特色
* 額外擴充24720個中文字元、字詞，強化模型處理繁體中文的能力
* 嚴格把關模型的訓練資料，提升模型生成資料的可信任性和適用性
* 針對自動摘要、寫信、寫文章、中翻英、英翻中等辦公室常用任務做加強
* 針對台灣在地文化、用語、國情等知識做加強
* 具備多輪問答對話能力

# 應用範例
| 任務 | 使用者輸入 | 模型輸出 |
| --- | -------- | ------- |
| 寫文章 | 請以以下內容為基礎，寫一篇文章：撰寫一篇作文，題目為《一張舊照片》，內容要求為：選擇一張令你印象深刻的照片，說明令你印象深刻的原因，並描述照片中的影像及背後的故事。記錄成長的過程、與他人的情景、環境變遷和美麗的景色。 | 以下是根據指令創作的一篇作文：<br><br>《一張舊照片》<br><br>在我塵封已久的家族相簿中，有一張特別吸引我的舊照片，那張照片記錄了我們家族成員在過往美好時光的歡聚，至今仍舊令人回味無窮。這張照片是我奶奶在二十多年前舉辦的一場家族聚會上所拍下的，照片中的人物包括了我的父母、祖父母、叔叔、姑姑和表哥等，大家臉上洋溢著幸福的笑容，彷彿時光靜止般地美好。<br><br>照片中的場景十分溫馨，大家圍坐在一張長方形的餐桌上，桌上擺滿了美味的食物和飲料。桌上的菜餚是傳統中式的佳餚，有香噴噴的烤全魚、嫩滑的雞肉和鮮甜的蔬菜，這些菜餚是當年奶奶親自烹調的，她手藝精湛，讓每個人都吃得津津有味。<br><br>最讓我印象深刻的是，照片中還拍到了我年幼時的模樣。我坐在桌子的另一端，手裡拿著一碗湯，臉上帶著滿足的笑容。那時的我才剛滿周歲，對於這場盛大的家族聚會還感到十分新奇。從這張照片中，我能感受到當年家族成員間的親密和溫暖，即使過了這麼多年，那份情感卻依然牢固地存在著。<br><br>這張照片背後有著動人的故事。在那個時代，我的祖父母和父母都還在讀中學，他們每天都會放學後到農田裡幫忙，辛勤地耕作以維持一家人的生計。儘管生活條件並不富裕，但他們仍舊保持著樂觀的態度和對生活的熱愛。每年到了秋天，只要收獲季節來臨，他們就會舉辦家族聚會，邀請所有親戚朋友前來共享豐收的喜悅。<br><br>隨著歲月的流逝，我逐漸長大，開始工作和生活。每次回鄉，我都會抽空去探望老人家，聽聽他們當年的往事，感受那段刻骨銘心的時光。而這張舊照片，也將一直陪伴著我，成為我珍貴回憶的一部分。它見證了我們的成長和變遷，也記錄下了那些難以忘懷的美好時刻。<br><br>這張照片不僅展示了家族的親情和溫暖，還折射出那個時代人們勤勞樸實的生活方式和對傳統的尊重。如今，隨著社會的快速發展，許多傳統的美德和風俗正在逐漸消失。我們應該好好珍惜這樣的回憶和文化，將它們傳承下去，讓後代子孫也能感受到那份來自歷史的溫情和傳承。<br><br>因此，我決定將這張照片好好保管起來，並常常拿出來看。它不僅是一張舊照片，更是一段寶貴的回憶和家族精神的象徵。我希望未來能有機會重現當年的盛況，再一次聚在一起，分享彼此的生活和故事，讓那份親情和友情繼續在時光中蔓延，永不消逝。 |
| 寫信   | 請以品牌經理的身份，給廣告公司的創意總監寫一封信，提出對於新產品廣告宣傳活動的創意建議。 | 尊敬的創意總監：<br><br>我寫這封信是為了向您提出一些關於我們新產品廣告宣傳活動的創意建議。我們公司即將推出一款全新的產品，為了確保它在市場上取得成功，我們希望透過一個引人注目的廣告宣傳活動來吸引消費者的注意。<br><br>在考慮廣告的創意和策略時，有幾個因素需要納入考量。首先，我們要針對目標客群進行研究，以瞭解他們的需求和喜好。其次，我們要確保廣告內容具有吸引力和說服力，能引起目標客群的共鳴。最後，我們要利用各種媒體平臺和數位行銷工具，以擴大廣告的影響力。<br><br>基於這些因素，我提出以下幾點創意建議：<br><br>1. 產品定位：我們可將這款新產品定位為高端、環保、健康和時尚的代表，強調其獨有的功能和特色。在廣告中，我們可以透過生動的視覺效果和簡潔的語言來傳達這些特點。<br>2. 故事行銷：在廣告中講述一個與產品功能相關的動人故事，讓消費者能更深入地瞭解產品所帶來的生活變化。例如，我們可以講述一位忙碌的職業婦女，如何使用我們的新產品在工作和生活中取得平衡的故事。<br>3. 名人效應：邀請一位受歡迎的公眾人物或意見領袖擔任產品代言人，利用他們的影響力來推廣產品。這不僅可以增加產品曝光度，還能讓更多消費者信任和信賴產品。<br>4. 跨界合作：與一些相關產業（如時尚、環保、健康等）進行跨界合作，共同推出限量版或聯名產品。這種合作不僅能吸引不同領域的消費者，還能為產品帶來更多話題性和收藏價值。<br>5. 數位行銷：充分利用社群媒體、搜尋引擎和電郵行銷等數位工具，在整個廣告宣傳過程中保持一致性的訊息和形象。我們也可製作一系列短視頻和線上活動，以增加消費者參與度和品牌忠誠度。<br>6. 創新形式：嘗試使用新穎的廣告形式，如AR（擴增實境）、VR（虛擬實境）和360度影片等，給消費者帶來全新的廣告體驗。這種創新形式不僅能吸引消費者目光，還能提高產品在市場上的辨識度。<br>7. 活動參與：在廣告宣傳活動中加入互動環節，如產品試用、抽獎和優惠券等，鼓勵消費者積極參與並分享他們的體驗。這將有助於口碑傳播，進一步擴大產品影響力。<br><br>綜合以上建議，我希望我們能製定出一套全面而富有創意的廣告宣傳活動計劃，以最大限度地提升新產品在市場上的競爭力。如果您有任何疑問或需要進一步討論，歡迎隨時與我聯絡。謝謝您的關注和支援！<br><br>祝商祺！<br><br>您的品牌經理<br><br>（註：此信件可根據實際情況和產品特點進行調整） |
| 摘要   | 請將這篇文章精簡條理化:「產業創新條例第10條之2及第72條條文修正案」俗稱「台版晶片法」,針對半導體、電動車、5G等技術創新且居國際供應鏈關鍵地位公司,提供最高25%營所稅投抵優惠,企業適用要件包含當年度研發費用、研發密度達一定規模,且有效稅率達一定比率。<br>為因應經濟合作暨發展組織(OECD)國家最低稅負制調整,其中有效稅率門檻,民國112年訂為12%,113年料將提高至15%,但仍得審酌國際間最低稅負制實施情形。<br>經濟部官員表示,已和財政部協商進入最後階段,除企業研發密度訂在6%,目前已確認,企業購置先進製程的設備投資金額達100億元以上可抵減。<br>財政部官員表示,研商過程中,針對台灣產業與其在國際間類似的公司進行深入研究,在設備部分,畢竟適用產創10之2的業者是代表台灣隊打「國際盃」,投入金額不達100億元,可能也打不了。<br>至於備受關注的研發費用門檻,經濟部官員表示,歷經與財政部來回密切討論,研發費用門檻有望落在60億至70億元之間。<br>財政部官員指出,研發攸關台灣未來經濟成長動能,門檻不能「高不可攀」,起初雖設定在100億元,之所以會調降,正是盼讓企業覺得有辦法達得到門檻、進而適用租稅優惠,才有動力繼續投入研發,維持國際供應鏈關鍵地位。<br>經濟部官員表示,因廠商研發費用平均為30、40億元,其中,IC設計業者介於30億至60億元範圍,若將門檻訂在100億元,符合條件的業者較少、刺激誘因不足;此外,若符合申請門檻的業者增加,將可提高企業在台投資金額,財政部稅收也能因此獲得挹注。<br>IC設計業者近日頻頻針對產創10之2發聲,希望降低適用門檻,加上各國力拚供應鏈自主化、加碼補助半導體產業,經濟部官員表示,經濟部和財政部就產創10之2達成共識,爭取讓更多業者受惠,盼增強企業投資力道及鞏固台灣技術地位。<br>財政部官員表示,租稅獎勵的制定必須「有為有守」,並以達到獎勵設置目的為最高原則,現階段在打「國內盃」的企業仍可適用產創第10條、10之1的租稅優惠,共同壯大台灣經濟發展。<br>經濟部和財政部正就研發費用門檻做最後確認,待今明兩天預告子法之後,約有30天時間,可與業界進一步討論及調整,盼產創10之2能在6月上路。 |  台灣「產業創新條例」的修正案，又稱「台版晶片法」,旨在支持半導體、電動車及5G技術領先企業的創新。新政策提供最高25%的所得稅抵免，企業需滿足當年度研發費用達一定規模、研發密度超過6%以及有效稅率達一定比率等條件。因應國際間對企業最低稅負制度的調整，台灣的門檻預計分別於2023年和2024年達到12%和15%。目前，與財政部討論後，確定100億元的設備投資抵免是可行的誘因，且研發費用門檻預計會在60至70億元之間。對於降低門檻的要求，經濟部和財政部已達成共識，旨在擴大受惠範圍並鼓勵企業投資以維持供應鏈的關鍵地位。此外，針對IC設計業者的訴求，也考慮調降門檻。預計此法案將在近期內實施，相關討論和調整將在預告期後進一步進行。  |
| 翻譯   | 以下提供英文內容，請幫我翻譯成中文。Dongshan coffee is famous for its unique position, and the constant refinement of production methods. The flavor is admired by many caffeine afficionados. | 東山咖啡以得天獨厚的地位，不斷精研的製作工藝著稱，風味獲諸多咖啡愛好者推崇。 |

# 使用說明
* 範例程式
    * 範例程式與文件後續會釋出到github
* tokenizer 必須設成 slow mode
    ```python
    tokenizer = AutoTokenizer.from_pretrained("taide/TAIDE-LX-7B-Chat", use_fast=False)
    ```
* prompt 樣版
    * 一般問答用法
        ```python
        f"<s>[INST] {question} [/INST]"
        ```
        * 將 {question} 替換成使用者的輸入
    * 加入 system prompt 的用法
        ```python
        f"<s>[INST] <<SYS>>\n{sys}\n<</SYS>>\n\n{question} [/INST]"
        ```
        * 將 {sys} 替換成指令，例如：你是一個來自台灣的AI助理，你的名字是 TAIDE，樂於以台灣人的立場幫助使用者，會用繁體中文回答問題。
        * 將 {question} 替換成使用者的問題
    * 多輪問答用法
        ```python
        f"<s>[INST] <<SYS>>\n{sys}\n<</SYS>>\n\n{question1} [/INST] {model_answer_1} </s><s>[INST] {question2} [/INST]"
        ```
        * 將 {sys} 替換成指令
        * 將 {question1} 替換成使用者的問題1
        * 將 {model_anwer_1} 替換成模型的回答1
        * 將 {question2} 替換成使用者的問題2
* Huggingface Chat 樣板
    * 一般問答用法
        ```python
        chat = [
            {"role": "user", "content": "{question}"},
        ]
        prompt = tokenizer.apply_chat_template(chat)
        ```
        * 將 {question} 替換成使用者的輸入
    * 加入 system prompt 的用法
        ```python
        chat = [
            {"role": "system", "content": "{sys}"},
            {"role": "user", "content": "{question}"},
        ]
        prompt = tokenizer.apply_chat_template(chat)
        ```
        * 將 {sys} 替換成指令，例如：你是一個來自台灣的AI助理，你的名字是 TAIDE，樂於以台灣人的立場幫助使用者，會用繁體中文回答問題。
        * 將 {question} 替換成使用者的問題
    * 多輪問答用法
        ```python
        chat = [
            {"role": "system", "content": "{sys}"},
            {"role": "user", "content": "{question1}"},
            {"role": "assistant", "content": "{model_anwer_1}"},
            {"role": "user", "content": "{question2}"},
        ]
        prompt = tokenizer.apply_chat_template(chat)
        ```
        * 將 {sys} 替換成指令
        * 將 {question1} 替換成使用者的問題1
        * 將 {model_anwer_1} 替換成模型的回答1
        * 將 {question2} 替換成使用者的問題2

# 訓練方法
* 軟硬體規格
    * 國網中心 H100
    * 訓練框架: PyTorch
* 資料前處理
    * 字元標準化
    * 去除重覆
    * 去除雜訊
        * 網頁資料的html tag、javascript
        * 非標準字元或亂碼
        * 字數過短的文章
        * 去除文章中的特定格式，如為排版增加的換行
    * 去除個資，如email、電話
    * 去除不當文字，如賭博、色情等
* 擴充字元字詞
    * 強化繁體中文輸入、輸出的效能，擴充資料包含下列2部分
        * 從[教育部異體字字典正字表](https://dict.variants.moe.edu.tw/appendix.jsp?ID=1&ID=0)獲取中文字元
        * 從繁中維基百科、新聞、中文common crawl資料抽取 500 萬條超過 100 個字元的句子(2.1G)，訓練中文字詞的 tokenizer
* 持續預訓練 (continuous pretraining, CP)
    * 補充大量來源可信賴的繁體中文知識
    * 超參數 (hyper parameters)
        * optimizer: AdamW
        * learning rate: 1e-4
        * batch size: 1M tokens
        * epoch: 1
* 微調 (fine tune, FT)
    * 讓模型可針對繁體中文提問回答問題
    * 超參數 (hyper parameters)
        * optimizer: AdamW
        * learning rate: 5e-5
        * batch size: 256K tokens
        * epoch: 3

# 訓練資料
* 持續預訓練資料(資料量約為140G)
| 資料集 | 資料描述 |
| --- | -------- |
| 訴訟資料 | 《[司法院裁判書](https://judgment.judicial.gov.tw/FJUD/default.aspx)》自2013年1月至2023年12月各級法院民事、刑事、行政訴訟資料。 |
| 中央社 | 《[中央社中文新聞](https://www.cna.com.tw/)》資料集含中央社自1993年6月至2023年06月，共30年份之每日新聞文章。內容涵蓋國內外政治、社會、財經、文教、生活等領域。 |
| ETtoday 新聞雲 | 《[ETtoday新聞雲](https://www.ettoday.net/)》資料，包含自2011年10月至 2023年12月的資料。 |
| 立法院公報 | 《[立法院公報](https://ppg.ly.gov.tw/ppg/)》包含自第8屆第1會期至第10屆第7會期之公報資料。 |
| 出版商網站書籍介紹 | 包含[三采](https://www.suncolor.com.tw/)、[Gotop](https://www.gotop.com.tw/)出版商網站上的書籍簡介。 |
| GRB 研究計畫摘要 | [GRB](https://www.grb.gov.tw/)為收錄由政府經費補助之研究計畫及其成果報告的資訊系統，此資料集主要收錄 1993年至 2023年之研究計畫摘要以及研究報告摘要，含中文及其英文對照。 |
| 學術會議論文摘要 | 收錄《[學術會議論文摘要資料庫](https://sticnet.stpi.narl.org.tw/sticloc/ttscalle?meet:)》中自1988至2009年由台灣所舉辦之學術會議論文。 |
| 光華雜誌 | 《[台灣光華雜誌](https://www.taiwan-panorama.com/)》含自1993年7月至2023年6月的文章，共30年份。內容著重於我國文化、觀光與民情等。 |
| 樂詞網 | 《[樂詞網](https://terms.naer.edu.tw/)》涵蓋文理領域約187萬則學術名詞及其譯名對照。 |
| 各部會資料 | 包含行政院「[國情簡介](https://www.ey.gov.tw/state/)」、文化部「[國家文化記憶庫](https://memory.culture.tw/)」、國發會「[檔案支援教學網](https://art.archives.gov.tw/index.aspx)」、交通部「[交通安全入口網](https://168.motc.gov.tw/)」等部會網站資料之部分資料。 |
| 今周刊 | 《[今周刊](https://www.businesstoday.com.tw/)》為一以財經為主的週刊雜誌，此資料集涵蓋2008年1月至2023年7月的文章。 |
| 教育部國語辭典、成語辭典 | 包含以下三項資料:<br>[教育部《成語典》](https://dict.idioms.moe.edu.tw/search.jsp?webMd=1&la=0)，含5,338條成語，內容包含每條成語的釋義、典故原文及其白話說明、用法說明、例句等。<br>[教育部《重編國語辭典修訂本》](https://dict.revised.moe.edu.tw/?la=0&powerMode=0)，收錄中文單字及各類辭彙，包含讀音、部首、釋義等資訊，共約165,539筆資料。<br>[教育部《國語辭典簡編本》](https://dict.concised.moe.edu.tw/?la=0&powerMode=0)，為《重編國語辭典修訂本》的簡編版本，共45,247筆資料。 |
| 科技大觀園資料 | 含《[科技大觀園網站](https://scitechvista.nat.gov.tw/)》上的科學新知以及科普文章。 |
| iKnow 科技產業資訊室 | 《[科技產業資訊室](https://iknow.stpi.narl.org.tw/)（iKnow）》提供台灣及全球的科技市場趨勢、策略分析、專利知識，及技術交易資訊，專注於科技產業的創新與發展，包含自 2008 年至 2023 年。 |
| 科學發展月刊 | 《[科學發展月刊](https://ejournal.stpi.narl.org.tw/sd)》為國科會為推廣科學教育而出版的科普刊物，含自2004年10月至2020年12月之科普文章；2021年起，以《[科技魅癮](https://www.charmingscitech.nat.gov.tw/)》季刊重新出發，提供國際關注科技議題的新知文章。 |
| 法規資料庫 | 《[法規資料庫](https://law.moj.gov.tw/)》含截自 112 年 10 月各政府部門最新發布之中央法規、行政規則、法規命令草案及地方自治法規等。 |
| 各地政府旅遊網 | 涵蓋台灣部分縣市地方政府觀光旅遊網站上之部分資料。 |
| 國教院課程綱要(十二年國教) | 含十二年國教課程綱要之總綱以及各級學校不同科目之課程綱要。 |
| 中央社譯名檔資料庫 | 《中央社譯名檔資料庫》蒐集中央社新聞業務上翻譯過的中外姓氏、人名、組織、地名等譯名對照。 |
| 童話書 | 共 20 本童話書，含湯姆歷險記、小飛俠、愛麗絲夢遊仙境、長腿叔叔等。 |
| RedPajama-Data-V2 | 從國外開放多國語言語料庫 [RedPajama-Data-v2](https://github.com/togethercomputer/RedPajama-Data) 取出英文資料 |
| MathPile-commercial | 國外開放數學語料庫 [MathPile-commercial](https://huggingface.co/datasets/GAIR/MathPile_Commercial) |
| 中文維基百科 | 《[中文維基百科](https://zh.wikipedia.org/zh-tw/%E4%B8%AD%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91)》截至2023年1月所有條目的內容。 |
| github-code-clean | 為 github 開源程式碼資料集，去除unlicense的程式碼和文件。 |
* 微調資料
    * TAIDE團隊訓練llama2系列模型來產生微調資料資料，產生的任務包含世界知識、創意寫作、普通常識、翻譯、摘要、程式、台灣價值等單輪或多輪對話問答共 128K 筆。微調資料後續會對外釋出。

# 模型評測
* taide-bench
    * 評測資料
        * 寫文章、寫信、摘要、英翻中、中翻英，共500題
        * 資料連結: [taide-bench](https://huggingface.co/datasets/taide/taide-bench)
    * 評測方法
        * gpt4評分
        * 評分程式: [taide-bench-eval](https://github.com/taide-taiwan/taide-bench-eval)
    * 評測分數
| 模型 | 中翻英 | 英翻中 | 摘要 | 寫文章 | 寫信 | 平均 |
| --- | ----- | ----- | ---- | ---- | ---- | --- |
| TAIDE-LX-7B-Chat | 7.165 | 7.685 | 7.720 | 9.635 | 9.110 | 8.263 |
| GPT3.5 | 8.880 | 8.810 | 7.450 | 9.490 | 8.750 | 8.676 |
| LLAMA2 7B | 6.075 | 4.475 | 5.905 | 2.625 | 3.040 | 4.424 |
| LLAMA2 13B | 6.480 | 6.135 | 6.110 | 2.565 | 3.000 | 4.858 |
| LLAMA2 70B | 6.975 | 6.375 | 6.795 | 2.625 | 2.990 | 5.152 |

# 授權條款
* [TAIDE L 類模型社群授權同意書](https://drive.google.com/file/d/1FcUZjbUH6jr4xoCyAronN_slLgcdhEUd/view?usp=drive_link)

# 免責聲明
* LLM 模型由於設計架構的限制，以及資料難免有偏誤，語言模型的任何回應不代表 TAIDE 立場，使用前需要額外加入安全防護機制，且回應內容也可能包含不正確的資訊，使用者請勿盡信。

# 開發團隊
* [https://taide.tw/index/teamList](https://taide.tw/index/teamList)

# 相關連結
* [TAIDE官網](https://taide.tw/index)
* [TAIDE Huggingface](https://huggingface.co/taide)
* [TAIDE Github](https://github.com/taide-taiwan)
* [Kuwa AI](https://kuwaai.org/)

# Citation
* [TAIDE官網](https://taide.tw/index)
>>>>>>> 87e74f5de0be96387524c1197e544e7f94d3e891
