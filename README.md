# 🤖 My LLM Chatbot

A web-based chatbot powered by Facebook’s BlenderBot using Hugging Face Transformers. This app processes user inputs and generates human-like responses using LLMs and Transformers.

---

## 🚀 Features

- Conversational AI with contextual memory  
- Powered by BlenderBot-400M from Meta  
- Web frontend built with **HTML**, **CSS**, and **JavaScript**  
- **Flask** backend for message routing  
- Uses **Hugging Face Transformers** library  

---

## 🧠 How It Works

1. User sends a message via the frontend  
2. Flask backend receives and routes the message to chatbot logic  
3. BlenderBot generates a response using the Transformers model  
4. Response is rendered back to the user interface  

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/my-llm-chatbot.git
cd my-llm-chatbot

python -m venv .venv
source .venv/Scripts/activate  # For Windows
# or
source .venv/bin/activate      # For macOS/Linux

pip install -r requirements.txt
python app.py
```

📁 Folder Structure
```bash
├── app.py              # Flask app
├── chatbot.py          # LLM logic using BlenderBot
├── requirements.txt
├── templates/
│   └── index.html      # Frontend HTML
├── static/
│   ├── css/
│   │   └── style.css   # Styling
│   ├── script.js       # Frontend JS
│   └── favicon.ico
```

🧪 Test via API
```bash
curl -X POST -H "Content-Type: application/json" \
     -d "{\"prompt\": \"Hello!\"}" \
     http://127.0.0.1:5000/chatbot
```

🔗 Model Info
Model: facebook/blenderbot-400M-distill

Library: Hugging Face Transformers

Framework: PyTorch
