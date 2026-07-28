# 👁️ VisionAssist AI

> **Gesture-Controlled Agentic Personal Assistant for Hands-Free Computer Interaction**

VisionAssist AI is an AI-powered desktop assistant that enables users to control their computer using hand gestures and voice commands. The system combines Computer Vision, Artificial Intelligence, and Agentic AI to perform real-world tasks such as opening applications, reading documents, searching the web, OCR-based text extraction, and voice interaction.

The project is designed to provide a hands-free and intelligent user experience by integrating gesture recognition with an autonomous AI agent.

---
## ✨ Features

- 🖐️ Hand gesture-based system control using MediaPipe.
- 🎤 Voice command support with Speech Recognition.
- 🤖 Agentic AI workflow powered by LangGraph and Google Gemini.
- 📄 PDF document reading and intelligent summarization.
- 🔍 OCR-based text extraction from images.
- 📂 File and folder management through natural language commands.
- 🌐 Open websites and search the web using voice instructions.
- 💻 Launch desktop applications such as VS Code and File Explorer.
- 🔊 Text-to-Speech responses for interactive conversations.
- 💬 Conversation history management for better user interaction.

---
## 🛠️ Tech Stack

### Frontend
- React (Vite)
- Tailwind CSS

### Backend
- FastAPI
- Python

### Artificial Intelligence
- Google Gemini API
- LangGraph

### Computer Vision
- OpenCV
- MediaPipe Hands

### Speech Processing
- SpeechRecognition
- pyttsx3

### Document Processing
- PyMuPDF (fitz)
- OCR

### Database
- SQLite

---
## 📁 Project Structure
```text
VisionAssist-AI
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── gestures/
│   │   ├── prompts/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── speech/
│   │   ├── tools/
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│   │
│   └── package.json
│
└── README.md
```

---
## 🖐️ Gesture Controls

| Gesture | Action |
|----------|--------|
| ✋ Open Palm | Activate VisionAssist AI |
| ☝️ Index Finger | Start Listening |
| 👍 Thumbs Up | Confirm / Execute Command |
| 👎 Thumbs Down | Listen Again |
| ✊ Fist | Deactivate Assistant |

---
## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/srishtisharma07/VisionAssist-AI.git
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The backend runs on **FastAPI**, while the frontend runs on **React (Vite)**.

---
## 🔮 Future Enhancements

- Improve gesture recognition accuracy
- Add more AI-powered personal assistant capabilities
- Add multilingual voice support
- Improve UI/UX design
- Add cloud deployment support


## 👩‍💻 Author

**Srishti Sharma**

B.Tech Computer Science Engineering  
Artificial Intelligence & Machine Learning


## 📄 License

This project is for educational purposes.
