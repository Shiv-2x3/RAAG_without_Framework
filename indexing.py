from chuncking import chunck_text
from embeddings import embbed
from vector_store import SimpleVectorStore

def build_index(documents : list[str]) -> SimpleVectorStore:
    store = SimpleVectorStore()

    for doc in documents:
        chunks = chunck_text(doc)
        for chunk in chunks:
            vector = embbed(chunk)
            store.add(chunk , vector)

    return store

