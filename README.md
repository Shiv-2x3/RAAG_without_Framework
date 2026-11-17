# A small local RAG demo

This project is a simple way to see how retrieval-augmented generation (RAG)
works. It takes a question, finds the most relevant parts of a document, and
asks a local language model to answer using those parts.

Everything runs through Ollama on your machine. You don't need an OpenAI API
key or a cloud model.

## What happens when you ask a question?

1. The project splits its source text into smaller, overlapping chunks.
2. Ollama turns each chunk into an embedding, a list of numbers that represents
   its meaning.
3. When you enter a question, the project embeds it and finds the closest
   chunks using cosine similarity.
4. The selected text and your question are sent to the local chat model, which
   writes an answer based on that context.

The document currently included in [main.py](./main.py) is an overview of
Project Helios. You can replace it with your own text.

## What you need

- Python 3
- [Ollama](https://ollama.com/) installed and running
- The chat and embedding models pulled into Ollama

From a terminal, pull the default models:

```bash
ollama pull qwen2.5:3b
ollama pull nomic-embed-text
```

If Ollama isn't already running, start it in a separate terminal:

```bash
ollama serve
```

## Install and run

From the project directory:

```bash
cd RAG
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

When prompted, enter a question about the included document.

## Choosing other Ollama models

The defaults are `qwen2.5:3b` for chat and `nomic-embed-text` for embeddings.
You can change them with environment variables or put them in a `.env` file in
this directory:

```dotenv
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_CHAT_MODEL=qwen2.5:3b
OLLAMA_EMBEDDING_MODEL=nomic-embed-text
```

Pull any models you choose with `ollama pull <model-name>` before running the
app. The embedding model must support Ollama's embeddings API.

## Project files

- `main.py` runs the example and builds the prompt.
- `chuncking.py` splits text into chunks (the current size and overlap are
  measured in characters).
- `embeddings.py` connects to Ollama and creates embeddings.
- `indexing.py` embeds the document chunks and adds them to the store.
- `vector_store.py` keeps vectors in memory and ranks chunks by similarity.

This is a learning project: the vector store is temporary, so the document is
embedded again each time you start the program. It doesn't use a database or
save an index to disk.
