# 🔍 LLM RAG Project (Local - Ollama)

Question-answering pipeline using local LLMs (Mistral/LLaMA2) via Ollama, context retrieval (RAG), and vector database (FAISS).

## 🚀 How to Run

```bash
# Clone the repository
$ git clone <repo>
$ cd llm_rag_project

# Install poetry (if not already installed)
$ curl -sSL https://install.python-poetry.org | python3 - --version 1.7.1

# Install dependencies
$ poetry install

# Activate shell
$ poetry shell

# Run the system (no API key needed)
$ python -m app.main
```

## 🧠 Requirements

- [Install Ollama](https://ollama.com/download) (macOS, Linux, Windows)
- Pull a model (Mistral or LLaMA2):

```bash
ollama pull mistral
# or
ollama pull llama2
```

## ✅ Pre-commit and Tests

```bash
# Install pre-commit hooks
$ pre-commit install

# Run tests
$ poetry run pytest
```

## 📁 Structure

- `app/`: main scripts (pipeline, utilities)
- `data/`: knowledge base documents
- `tests/`: unit tests

## 🧠 Tech Stack

- LangChain (core + community)
- Mistral/LLaMA2 via Ollama
- FAISS
- Python 3.11.8+
- Poetry, Pytest, Ruff, Black, Pre-commit

## 🂡 Flashcards
[![Visit Website](https://img.shields.io/badge/Open-Click%20Here-blue)](https://ankipro.net/shared_deck/v2_pajQbEpeeL_4961509)

---

Feel free to contribute with ideas, issues or improvements! 💡
