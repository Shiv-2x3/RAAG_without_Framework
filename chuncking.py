def chunck_text(text :str , chunk_size: int = 500 , overlap: int = 50) -> list[str]:
    """
    split text into overlaping chunks by char count.
    chunk_size and overlap are in char not in token
    for production use swap to tokenizer.
    """
    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("chunk_size must be positive and overlap must be smaller than chunk_size")

    start = 0
    chunks = []
    text = text.strip()

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk.strip())
        if end >= len(text):
            break
        start += chunk_size - overlap
    return [c for c in chunks if c]   