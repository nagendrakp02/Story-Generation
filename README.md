# 📖 AI Story Generator

An AI-powered **Story Generation App** built with **Streamlit**, **LangChain**, and **Groq LLMs**.  
This project lets you input a **topic** and generates a creative story in your chosen **language**.

---

## 🚀 Features
- Generate stories based on any **topic**.
- Supports **multiple languages** (default: English).
- Simple, clean **Streamlit UI**.
- Hybrid support (local + cloud deployment).
- Modular project structure (Graphs, LLMs, Nodes, States).

---

## 📂 Project Structure
.
├── app.py # Main Streamlit app entry point
├── main.py # (Optional) CLI entry point
├── .env # Environment file for local API keys
├── README.md # Project documentation
├── requirements.txt # Python dependencies
├── pyproject.toml # Project config
├── src
│ ├── graphs
│ │ ├── init.py
│ │ └── graph_builder.py # Graph setup for LangChain
│ ├── llms
│ │ ├── init.py
│ │ └── groqllm.py # Groq LLM integration
│ ├── nodes
│ │ ├── init.py
│ │ └── story_node.py # Node logic for story generation
│ └── states
│ ├── init.py
│ └── storystate.py # Defines story state object
└── .gitignore

## 🛠️ Dependencies
- Python 3.8+
- Streamlit
- Langchain
- Groq API

## 🧑‍💻 Author
- **Nagendra K P** | [GitHub](https://github.com/nagendrakp02)
