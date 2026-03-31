# 🤖 Chatbot with History

> **A Streamlit chat application powered by LangGraph with persistent conversation memory**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Core-green?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48cmVjdCB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgZmlsbD0iIzAwMDAiLz48L3N2Zz4=)](https://www.langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 🎯 Live Demo

Experience the chatbot in action:  
👉 **[Open Chatbot with History](https://chatbot-with-history-gmdy2dbam4azdxr4lf6pun.streamlit.app/)**

---

## ✨ Features

- 💬 **Intelligent Conversational AI** - Powered by Groq's Qwen model for fast, intelligent responses
- 📜 **Persistent Chat History** - SQLite-backed conversation memory that persists across sessions
- 🔄 **Multi-threaded Conversations** - Create and manage multiple independent chat threads
- 👤 **User Context Recognition** - Chatbot learns and remembers your name and role from conversations
- ⚡ **Real-time Streaming** - Stream AI responses as they're generated for responsive UX
- 🧹 **Smart Response Sanitization** - Removes internal reasoning and thinking tags for clean, concise outputs
- 📋 **Conversation Management** - Easy access to all previous conversations from the sidebar
- 🚀 **Graph-based Architecture** - Built with LangGraph for robust state management

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Web UI framework for interactive chat interface |
| **LangChain** | Prompt orchestration and message management |
| **LangGraph** | State graph and conversation routing |
| **Groq API** | Fast LLM inference (Qwen 3-32B model) |
| **SQLite** | Persistent conversation storage |
| **BeautifulSoup** | Web scraping support |

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Groq API key ([Get one here](https://console.groq.com))

### Step 1: Clone the Repository
```bash
git clone https://github.com/Kjagadeeshkumarreddy/chatbot-with-history.git
cd chatbot-with-history
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in the project root:
```
GROQ_API=your_groq_api_key_here
```

### Step 5: Run the Application
```bash
streamlit run chatBot_frontend.py
```

The application will open in your browser at `http://localhost:8501`

---

## 🎮 Usage

### Getting Started
1. **Start a New Chat** - Click the "New Chat" button in the sidebar to begin a new conversation
2. **Chat with the Bot** - Type your message in the input field and press Enter
3. **Personal Context** - Tell the bot your name or role in the conversation (e.g., "My name is Alice" or "I am a software engineer")
4. **Query Context** - Ask "What is my name?" or "What is my role?" and the bot will remember from your history

### Navigation
- **Browse History** - All your conversations appear in the "My Conversations" section of the sidebar
- **Switch Conversations** - Click any thread ID to load and continue a previous conversation
- **New Chat** - Start fresh with a clean slate by clicking "New Chat"

### Features in Action
- The chatbot maintains context throughout the conversation
- Responses are concise and direct
- Previous interactions are preserved even after closing the application
- Each conversation thread is isolated and independent

---

## 📁 Project Structure

```
chatbot-with-history/
├── chatBot_frontend.py          # Streamlit UI and user interface
├── chatBot_backend.py           # LangGraph logic and chat model
├── requirements.txt             # Python dependencies
├── chatbot.db                   # SQLite database (auto-generated)
├── .devcontainer/               # Dev container configuration
└── README.md                    # This file
```

### File Descriptions

| File | Description |
|------|-------------|
| **chatBot_frontend.py** | Streamlit application handling UI, session state, and conversation display |
| **chatBot_backend.py** | LangGraph-powered chatbot with message routing, context extraction, and LLM integration |
| **requirements.txt** | All Python package dependencies |

---

## 🔧 How It Works

### Architecture
1. **Frontend Layer** - Streamlit handles the user interface and manages session state
2. **State Management** - Conversations are tracked using unique thread IDs
3. **Backend Layer** - LangGraph manages message flow and LLM interactions
4. **Persistence** - SQLite checkpointer stores all messages and conversation state
5. **LLM Integration** - Groq API provides fast inference with the Qwen 3-32B model

### Conversation Flow
```
User Input
    ↓
Frontend (Streamlit)
    ↓
Backend (LangGraph)
    ↓
Context Extraction (Name/Role)
    ↓
LLM Processing (Groq)
    ↓
Response Sanitization
    ↓
Display & Storage
```

---

## 🚀 Future Improvements

- 🎨 **Enhanced UI/UX** - Add conversation themes and customizable styling
- 🔐 **User Authentication** - Support for user accounts with personalized histories
- 📊 **Analytics Dashboard** - Visualize conversation patterns and statistics
- 🌐 **Multi-language Support** - Support for multiple languages
- 📎 **File Uploads** - Allow users to upload and discuss documents
- 🔗 **Web Search Integration** - Enable real-time information retrieval
- 💾 **Export Conversations** - Export chats as PDF or text files
- 🎯 **Intent Recognition** - Advanced NLU for better context understanding
- ⚙️ **Model Switching** - Allow users to switch between different LLM providers

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request** with a description of your changes

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test your changes locally before submitting
- Update the README if adding new features

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

The MIT License allows you to use, modify, and distribute this software freely, as long as you include the license notice.

---

## 👨‍💻 Author

**Kjagadeeshkumarreddy**

- GitHub: [@Kjagadeeshkumarreddy](https://github.com/Kjagadeeshkumarreddy)
- Repository: [chatbot-with-history](https://github.com/Kjagadeeshkumarreddy/chatbot-with-history)

---

## 💡 Troubleshooting

### Issue: "GROQ_API key not found"
**Solution:** Make sure you've created a `.env` file with your Groq API key:
```bash
echo "GROQ_API=your_api_key" > .env
```

### Issue: "Database is locked"
**Solution:** This typically means multiple instances are running. Close all instances and try again.

### Issue: Conversations not loading
**Solution:** Verify that `chatbot.db` exists in the project directory and is not corrupted. Delete it to start fresh.

---

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Open an [Issue](https://github.com/Kjagadeeshkumarreddy/chatbot-with-history/issues)
3. Review [LangChain Documentation](https://python.langchain.com/)
4. Check [Streamlit Documentation](https://docs.streamlit.io/)

---

<div align="center">

**Made with ❤️ by Kjagadeeshkumarreddy**

⭐ If you found this project helpful, please consider giving it a star!

</div>
