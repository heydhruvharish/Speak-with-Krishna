# Speak with Krishna

**Speak with Krishna** is an AI-powered conversational chatbot inspired by the teachings and wisdom of Lord Krishna from ***Bhagavad Gita As It Is***.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant passages from *Bhagavad Gita As It Is* and provide context-aware responses based on its teachings.

## Live Demo

[Try Speak with Krishna](https://speak-with-krishna.streamlit.app/)

## Features

* AI-powered conversational interface
* Retrieval-Augmented Generation (RAG)
* Semantic search over *Bhagavad Gita As It Is*
* Vector embeddings using Sentence Transformers
* ChromaDB vector database for document retrieval
* Context-aware responses
* Session-based conversation history
* User authentication with Supabase
* Fast LLM inference using Groq
* Streamlit-based web interface

## How RAG Works

The chatbot uses the following pipeline:

```text
User Question
      ↓
Query Embedding
      ↓
Semantic Search
      ↓
ChromaDB Vector Store
      ↓
Relevant Passages from Bhagavad Gita As It Is
      ↓
LLM + Retrieved Context
      ↓
Generated Response
```

The **Bhagavad Gita As It Is** PDF is processed into smaller chunks. Each chunk is converted into a numerical embedding using a Sentence Transformer model and stored in ChromaDB.

When a user asks a question, the question is also converted into an embedding. ChromaDB retrieves the most semantically relevant passages from *Bhagavad Gita As It Is*. These passages are then provided to the language model as context for generating the response.

## Tech Stack

* **Python** — Core programming language
* **Streamlit** — Web application framework
* **Groq** — LLM inference
* **LangChain** — Document loading and text processing
* **Sentence Transformers** — Text embeddings
* **ChromaDB** — Vector database
* **Supabase** — Authentication and database
* **PyMuPDF** — PDF processing
* **bcrypt** — Password hashing


## RAG Pipeline

### 1. Document Processing

*Bhagavad Gita As It Is* is loaded and divided into smaller chunks using a recursive text splitter.

### 2. Embeddings

Each chunk is converted into a vector representation using the **all-MiniLM-L6-v2** Sentence Transformer model.

### 3. Vector Storage

The generated embeddings are stored in **ChromaDB** for efficient semantic similarity search.

### 4. Retrieval

When a user asks a question, the application converts the query into an embedding and retrieves the most relevant passages from *Bhagavad Gita As It Is*.

### 5. Generation

The retrieved passages are provided to the language model as context, allowing it to generate a response grounded in the retrieved content.

## Authentication

User authentication and application data are managed using **Supabase**. Passwords are securely hashed using `bcrypt`.

## Disclaimer

Speak with Krishna is an educational and experimental AI project inspired by *Bhagavad Gita As It Is*. Responses are AI-generated and may not represent the exact interpretation of the original text.

## Future Improvements

- Persistent chat history stored in Supabase
- Improved Sanskrit and Hindi OCR
- Voice-based interaction
- Conversation titles and chat search

## Author

**Dhruv Harish**

GitHub: [@heydhruvharish](https://github.com/heydhruvharish)

---

> *Speak with Krishna. Seek wisdom. Discover your path.*
