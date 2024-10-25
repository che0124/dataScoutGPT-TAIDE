document.getElementById('sendButton').addEventListener('click', sendMessage);
document.getElementById('sendURL').addEventListener('click', downloadFilesFromUrl);
document.getElementById('uploadPdfButton').addEventListener('click', uploadPDF);

async function sendMessage() {
  
  const userInput = document.getElementById('userInput').value;
  
  displayInput(userInput);
  document.getElementById('userInput').value = '';

  const formData = new FormData();
  formData.append('user_input', userInput);

  try {
    const response = await fetch('http://localhost:5000/chat', {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    displayResponse(data.response);
  } catch (error) {
    console.error('Error:', error);
    displayResponse(`Error: Unable to fetch response from server. ${error.message}`);
  }

}


function uploadPDF() {
  const pdfFile = document.getElementById('pdfFile').files[0];

  if (!pdfFile) {
    document.getElementById('uploadStatus').innerText = '請選擇一個 PDF 文件';
    return;
  }
  const formData = new FormData();
  formData.append('pdf_file', pdfFile);

  fetch('http://localhost:5000/upload_pdf', { 
    method: 'POST',
    body: formData,
  })
  .then(response => response.json())
  .then(data => {
    if (data.message) {
      document.getElementById('uploadStatus').innerText = 'PDF 上傳成功';
    } else {
      document.getElementById('uploadStatus').innerText = `PDF 上傳失败: ${data.message}`;
    }
  })
  .catch(error => {
    console.error('Error:', error);
    document.getElementById('uploadStatus').innerText = `PDF 上傳失败 ${error.message}`;
  });
}


function displayInput(userInput) {
  const chatbox = document.getElementById('chatbox');

  const userWrapper = document.createElement('div');
  userWrapper.classList.add('message-wrapper', 'user-message-wrapper');

  const userMessage = document.createElement('div');
  userMessage.classList.add('message', 'user-message');
  userMessage.innerText = userInput;

  userWrapper.appendChild(userMessage);

  chatbox.appendChild(userWrapper);

  chatbox.scrollTop = chatbox.scrollHeight;
}

function displayResponse(response) {
  const chatbox = document.getElementById('chatbox');

  const botWrapper = document.createElement('div');
  botWrapper.classList.add('message-wrapper', 'bot-message-wrapper');

  const botMessage = document.createElement('div');
  botMessage.classList.add('message', 'bot-message');
  botMessage.innerText = response;

  botWrapper.appendChild(botMessage);

  chatbox.appendChild(botWrapper);

  chatbox.scrollTop = chatbox.scrollHeight;
}


function downloadFilesFromUrl() {
  const url = document.getElementById('inputURL').value
  // 使用 jQuery 的 Ajax 加載目標 URL 的 HTML 內容
  const proxyUrl = 'https://cors-anywhere.herokuapp.com/';
  $.ajax({
      url: proxyUrl + url,
      method: 'GET',
      success: function (response) {
          // 將返回的 HTML 內容轉換為 jQuery 對象
          var htmlContent = $(response);

          // 選擇所有可能的文件鏈接（假設以常見文件類型結尾）
          var fileLinks = htmlContent.find("a[href$='.pdf'], a[href$='.doc'], a[href$='.docx'], a[href$='.xls'], a[href$='.xlsx'], a[href$='.zip'], a[href$='.odt'], a[href$='.ods']");

          // 遍歷每個文件鏈接
          fileLinks.each(function () {
              var link = $(this).attr('href'); // 獲取文件的 href 屬性
              var fileName = link.split('/').pop(); // 從 URL 提取文件名

              // 如果鏈接是相對路徑，則轉換為絕對路徑
              if (!link.startsWith('http')) {
                  var absoluteLink = new URL(link, url).href;
                  link = absoluteLink;
              }

              // 打印正在抓取的文件URL
              console.log('Downloading file from URL:', link);

              // 使用 Fetch API 下載文件並使用 FileSaver.js 保存文件
              fetch(proxyUrl + link)
                  .then(response => response.blob()) // 將響應轉換為 Blob
                  .then(blob => {
                      console.log('Downloaded:', fileName); // 顯示已下載的文件名
                      saveAs(blob, fileName); // 使用 FileSaver.js 的 saveAs 函數保存文件
                  })
                  .catch(error => console.error('Error downloading file:', error));
          });
      },
      error: function (error) {
          console.error('Error loading the page:', error);
      }
  });
}