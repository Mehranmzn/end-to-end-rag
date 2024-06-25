# End-to-End RAG Pipeline

Welcome to the End-to-End Retrieval-Augmented Generation (RAG) Pipeline project! This repository provides a complete solution for building, deploying, and interacting with a RAG pipeline, leveraging various modern technologies including LangChain, Pinecone, OpenAI, and Streamlit.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview

The End-to-End RAG Pipeline project is designed to facilitate the process of loading documents, creating embeddings, storing them in a vector store, and running queries against this store using a Language Model (LLM). This project integrates several components to provide a seamless experience for building and interacting with an RAG pipeline.

## Features

- **Document Loading:** Load documents from web URLs using `WebBaseLoader`.
- **Text Splitting:** Efficiently split documents into chunks with `RecursiveCharacterTextSplitter`.
- **Embedding Generation:** Generate embeddings using OpenAI's models.
- **Vector Store:** Store embeddings in Pinecone for fast retrieval.
- **Language Model Integration:** Utilize Groq's LLM for processing queries.
- **Guardrails:** Ensure safe and effective interactions with NeMo Guardrails.
- **Streamlit Interface:** User-friendly interface for interacting with the pipeline.

## Installation

### Prerequisites

- Python 3.8 or higher
- [Pinecone API Key](https://www.pinecone.io/)
- [OpenAI API Key](https://www.openai.com/)
- [Groq API Key](https://groq.com/)
- [LangSmith API Key](https://www.langsmith.com/)

### Setup

1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/end-to-end-rag.git
   cd end-to-end-rag

2. **Create and Activate Virtual Environment**
 ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
   or
   ```sh
   Pipfile
   ```
5. **Environment Variables**
   ```sh
   OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
```
5. **Running the Streamlit App**
```sh
streamlit run app.py
```
or
```sh
pipenv streamlit run app.py
```

**Project Structure:**
.
├── README.md
├── app.py
├── run.py
├── config
│   ├── actions.py
│   ├── config.py
│   ├── config.yml
│   ├── rails.co
│   └── ...
├── requirements.txt
└── .env


