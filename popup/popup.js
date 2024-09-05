document.getElementById('sendButton').addEventListener('click', sendMessage);

// 发送用户输入的消息和 PDF 文件到 Flask 后端
async function sendMessage() {
  const userInput = document.getElementById('userInput').value;
  const pdfFile = document.getElementById('pdfFile').files[0]; // 获取上传的文件

  if (!userInput || !pdfFile) {
    alert("Please enter a message and select a PDF file.");
    return;
  }

  displayInput(userInput)

  const formData = new FormData();
  formData.append('user_input', userInput);
  formData.append('pdf_file', pdfFile);

  try {
    const response = await fetch('http://localhost:5000/process_pdf', { // Flask 服务地址
      method: 'POST',
      body: formData,
    });

    const data = await response.json();
    displayResponse(data.response);
    document.getElementById('userInput').value = '';  // 清空输入框
  } catch (error) {
    console.error('Error:', error);
    displayResponse('Error: Unable to fetch response from server.');
  }
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


