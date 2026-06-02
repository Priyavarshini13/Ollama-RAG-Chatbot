# Ollama RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built using Ollama, Flask, and local GGUF models. The chatbot retrieves relevant information from a knowledge base and generates context-aware responses using a local Large Language Model.

## Features

* Local AI inference using Ollama
* Retrieval-Augmented Generation (RAG)
* Semantic search using embeddings
* Flask web application
* Responsive chat interface
* No external API dependency
* Privacy-friendly local execution

## Technologies Used

### Backend

* Python
* Flask
* Ollama

### Frontend

* HTML
* CSS
* JavaScript

### Models

* Embedding Model:

  * `hf.co/CompendiumLabs/bge-base-en-v1.5-gguf`
* Language Model:

  * `hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF`

## Project Structure

```text
OLLAMA/
│
├── rag_engine.py
├── server.py
├── cat-facts.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## How It Works

1. Load the knowledge base from `cat-facts.txt`
2. Generate embeddings for each text chunk
3. Store embeddings in a vector database
4. Convert user query into an embedding
5. Perform cosine similarity search
6. Retrieve the most relevant chunks
7. Provide retrieved context to the language model
8. Generate an accurate response

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd OLLAMA
```

### Install Dependencies

```bash
pip install flask flask-cors ollama
```

### Pull Required Models

```bash
ollama pull hf.co/CompendiumLabs/bge-base-en-v1.5-gguf
ollama pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF
```

## Running the Application

Start the Flask server:

```bash
python server.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## Example Query

```text
What is the average lifespan of a cat?
```

## Future Enhancements

* PDF document support
* Multiple knowledge bases
* Chat history
* User authentication
* Voice input/output
* Database integration
* Streaming responses

## Author

Priyavarshini V

## License

This project is developed for educational and learning purposes.
