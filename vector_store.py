import numpy as np

class SimpleVectorStore:
    def __init__(self):
        self.vectors: list[np.ndarray] = []
        self.chunks: list[str] = []
    def add(self , chunk : str ,  vector: list[float]):
        self.chunks.append(chunk)
        self.vectors.append(np.array(vector))
    def search(self , query_vector : list[float] , top_k : int = 3) -> list[tuple[str , float]]:
        query_vec = np.array(query_vector)
        scores = []
        for chunk , vec in zip(self.chunks , self.vectors):
            score = self._cosine_similarity(query_vec , vec)
            scores.append((chunk , score))
        scores.sort(key=lambda result: result[1], reverse=True)
        return scores[:top_k]
    @staticmethod
    def _cosine_similarity(a : np.ndarray , b : np.ndarray) -> float:
        denominator = np.linalg.norm(a) * np.linalg.norm(b)
        if denominator == 0:
            return 0.0
        return float(np.dot(a, b) / denominator)

    