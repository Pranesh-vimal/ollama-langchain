# Ollama-LangChain Integration

This repository demonstrates how to integrate [Ollama](https://ollama.ai/) with [LangChain](https://python.langchain.com/) to build powerful AI applications. It provides examples of basic usage, agent implementation, and Retrieval Augmented Generation (RAG) to help you get started with these technologies.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Agent Usage](#agent-usage)
  - [RAG Usage](#rag-usage)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Resources](#resources)

## Introduction

This repository showcases three main ways to use Ollama with LangChain:

1. **Basic Integration**: Simple example of using Ollama models with LangChain
2. **Agent Implementation**: Creating an agent with tools for file operations
3. **RAG (Retrieval Augmented Generation)**: Building a system to search and query documents

[Ollama](https://ollama.ai/) is an open-source framework for running large language models locally on your machine. [LangChain](https://python.langchain.com/) is a framework for developing applications powered by language models. Together, they allow you to build powerful AI applications that run locally.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) 3.8 or higher
- [Ollama](https://ollama.ai/download) (latest version)
- Required models pulled to your Ollama installation:
  - `deepseek-r1` (for basic example)
  - `llama3.2` (for agent and RAG examples)
  - `nomic-embed-text` (for embeddings in RAG example)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ollama-langchain.git
   cd ollama-langchain
   ```

2. Create a Python virtual environment:

   **macOS/Linux**:
   ```bash
   python3 -m venv venv
   ```

   **Windows**:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   **macOS/Linux**:
   ```bash
   source venv/bin/activate
   ```

   **Windows (Command Prompt)**:
   ```bash
   venv\Scripts\activate.bat
   ```

   **Windows (PowerShell)**:
   ```bash
   venv\Scripts\Activate.ps1
   ```

4. Install the required Python packages (with virtual environment activated):

   **Option 1: Direct installation**
   ```bash
   pip install langchain langchain-ollama langchain-community pydantic docx2txt PyPDF2 faiss-cpu
   ```
   
   **Option 2: Using requirements.txt**
   
   Alternatively, you can use a requirements.txt file to manage dependencies:
   
   Create a file named `requirements.txt` with the following content:
   ```
   langchain
   langchain-ollama
   langchain-community
   pydantic
   docx2txt
   PyPDF2
   faiss-cpu
   ```
   
   Then install the packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Ensure Ollama is running:
   ```bash
   ollama serve
   ```

6. Pull the required models:
   ```bash
   ollama pull deepseek-r1
   ollama pull llama3.2
   ollama pull nomic-embed-text
   ```

7. When you're done working with the project, you can deactivate the virtual environment:
   ```bash
   deactivate
   ```

## Project Structure

The repository is organized into three main directories:

- **`basic/`**: Contains a simple example of using Ollama with LangChain
  - `main.py`: Basic implementation of ChatOllama

- **`agent/`**: Implements an agent with tools for file operations
  - `main.py`: Agent implementation with FileManagementToolkit
  - `tools.py`: Custom tool for loading DOCX files

- **`rag/`**: Implements Retrieval Augmented Generation for document search
  - `rag.py`: Script to process documents and create a vector database
  - `search.py`: Script to search the vector database and answer questions

## Usage

### Basic Usage

The basic example demonstrates how to use Ollama with LangChain to create a simple chat application:

```bash
python basic/main.py
```

This script:
1. Creates a ChatOllama instance with the "deepseek-r1" model
2. Sets up a system message to identify gibberish words
3. Sends a human message "good morning"
4. Prints the result

You can modify the script to use different models or prompts:

```python
llm = ChatOllama(
    model="your-preferred-model",  # Change to any model you have pulled
    temperature=0.7,  # Adjust for more/less creative responses
)

messages = [
    ("system", "Your custom system message here"),
    ("human", "Your custom human message here"),
]
```

### Agent Usage

The agent example shows how to create an agent with tools for file operations:

```bash
python agent/main.py
```

This script:
1. Creates a ChatOllama instance with the "llama3.2" model
2. Sets up FileManagementToolkit for file operations
3. Adds a custom DocxFileLoad tool
4. Creates an agent with tool-calling capabilities
5. Runs the agent with a specific query

To use it with your own files:
1. Place your DOCX files in the repository directory
2. Modify the query in `agent/main.py`:

```python
result = agent_executor.invoke({"input": "Your custom query about your files"})
```

### RAG Usage

The RAG example demonstrates how to build a system for searching and querying documents:

1. First, process your documents to create a vector database:
   ```bash
   python rag/rag.py
   ```

   This script:
   - Uses OllamaEmbeddings to create embeddings
   - Processes text and PDF files from a specified directory
   - Creates a FAISS vector store
   - Saves the vector store to disk

   **Note:** You'll need to modify the `resumes_dir` path in `rag/rag.py` to point to your own directory containing documents:
   ```python
   resumes_dir = '/path/to/your/documents'
   ```

2. Then, search the vector database:
   ```bash
   python rag/search.py
   ```

   This script:
   - Loads the saved vector store
   - Creates a RetrievalQA chain
   - Answers questions based on the documents

   To ask your own questions, modify the query in `rag/search.py`:
   ```python
   answer = qa({"query": "Your question here"})
   ```

## Customization

### Using Different Models

You can use any model available in Ollama by changing the model name:

```python
llm = ChatOllama(
    model="your-model-name",  # e.g., "llama3", "mistral", etc.
    temperature=0.5,  # Adjust as needed
)
```

### Modifying Prompts

You can customize the prompts to suit your needs:

```python
prompt_template = """
Your custom prompt here.
Context: {context}
Question: {question}
"""
```

### Extending Functionality

To add new tools to the agent:

1. Create a new tool class in `agent/tools.py`
2. Add the tool to the tools list in `agent/main.py`

## Troubleshooting

### Common Issues

1. **Model not found error**:
   - Ensure Ollama is running (`ollama serve`)
   - Check if you've pulled the model (`ollama list`)
   - Pull the model if needed (`ollama pull model-name`)

2. **Memory issues with large documents**:
   - Reduce the chunk size in `rag/rag.py`
   - Process fewer documents at a time

3. **Slow performance**:
   - Consider using a smaller model
   - Reduce the number of documents or chunks processed

### Debugging Tips

- Add print statements to track the flow of execution
- Check the Ollama logs for any errors
- Verify that your file paths are correct

## Resources

- [Ollama Documentation](https://github.com/ollama/ollama/tree/main/docs)
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [FAISS Documentation](https://faiss.ai/index.html)

---

Happy coding! If you have any questions or issues, please open an issue on this repository.
