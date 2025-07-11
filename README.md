🤖 My LLM Chatbot
A web-based chatbot powered by Facebook’s BlenderBot using Hugging Face Transformers. This app processes user inputs and generates human-like responses using LLMs and Transformers.

🚀 Features
Conversational AI with contextual memory
Powered by BlenderBot-400M from Meta
Web frontend built with HTML, CSS, JS
Flask backend for message routing
Uses Hugging Face transformers library
🧠 How It Works
User sends a message via the frontend
Flask receives and routes it to the chatbot logic
BlenderBot generates a response via transformers
Response is rendered back to the UI
📦 Installation
git clone https://github.com/yourusername/my-llm-chatbot.git
cd my-llm-chatbot

python -m venv .venv
source .venv/Scripts/activate  # For Windows

pip install -r requirements.txt
python app.py
📁 Folder Structure

bash``` ├── app.py # Flask app ├── chatbot.py # LLM logic ├── requirements.txt ├── templates/ │ └── index.html ├── static/ │ ├── css/style.css │ ├── script.js │ └── favicon.ico


---

🧪 Test via API

bash```
curl -X POST -H "Content-Type: application/json" \
     -d "{\"prompt\": \"Hello!\"}" \
     http://127.0.0.1:5000/chatbot
🔗 Model Info

Model: facebook/blenderbot-400M-distill

Library: Hugging Face transformers

Framework: PyTorch

