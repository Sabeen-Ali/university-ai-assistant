# 🎓 University AI Assistant

An intelligent multi-agent AI assistant designed to support university students with academic guidance, information retrieval, question answering, and research assistance.

This project leverages Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), vector databases, and modular AI agents to create a scalable and extensible university support system.

---

# 🚀 Features

* 🤖 Multi-Agent Architecture
* 📚 Retrieval-Augmented Generation (RAG)
* 🧠 Intelligent Query Routing
* 🔍 Semantic Search with Vector Store
* 📄 Knowledge Base Integration
* ⚡ Modular and Scalable Design
* 🛠️ Easy Environment Configuration
* 💬 Natural Language Interaction

---

# 🏗️ Project Architecture

The system is built using multiple specialized agents:

| Agent            | Responsibility                                |
| ---------------- | --------------------------------------------- |
| `GeneralAgent`   | Handles general university-related questions  |
| `RAGAgent`       | Retrieves information from the knowledge base |
| `EvaluatorAgent` | Evaluates and validates responses             |
| `RouterAgent`    | Routes user queries to the appropriate agent  |
| `BaseAgent`      | Shared functionality for all agents           |

---

# 📂 Project Structure

```bash
my-ai-assistant/
│
├── agents/
│   ├── base_agent.py
│   ├── evaluator_agent.py
│   ├── general_agent.py
│   ├── rag_agent.py
│   └── router_agent.py
│
├── knowledge_base/
│
├── tools/
│   ├── rag_tool.py
│   └── vector_store/
│
├── venv/
├── .env
├── .env.example
├── graph.py
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Technologies Used

* Python
* LangChain
* OpenAI / LLM APIs
* Vector Databases
* RAG Architecture
* Git & GitHub

---

# 🛠️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sabeen-Ali/university-ai-assistant.git
```

## 2️⃣ Navigate to the Project Directory

```bash
cd university-ai-assistant
```

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory and add your API keys.

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

---

# ▶️ Running the Application

```bash
python main.py
```

---

# 💡 Example Use Cases

* Student academic assistance
* University FAQs
* Course guidance
* Research support
* Knowledge retrieval from documents
* AI-powered educational chatbot

---

# 📈 Future Improvements

* Web Interface Integration
* Voice Assistant Support
* Database Connectivity
* Authentication System
* Real-Time University Portal Integration
* Advanced Memory Management

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sabeen Ali**

* GitHub: [https://github.com/Sabeen-Ali](https://github.com/Sabeen-Ali)

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
