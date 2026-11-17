import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
    api_key="ollama",
)
embedding_model = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")
chat_model = os.getenv("OLLAMA_CHAT_MODEL", "qwen2.5:3b")

def embbed(text : str) -> list[float]:
    response = client.embeddings.create(
        model=embedding_model,
        input=text
    )
    return response.data[0].embedding