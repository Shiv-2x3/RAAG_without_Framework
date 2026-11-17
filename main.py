from chuncking import chunck_text
from embeddings import chat_model, client, embbed
from vector_store import SimpleVectorStore
from indexing import build_index

def answer_question(question : str , store : SimpleVectorStore , top_k : int = 3) -> str:
    query_vector = embbed(question)
    results = store.search(query_vector , top_k = top_k)
    context = "\n\n---\n\n".join(chunk for chunk , score in results)
    prompt = f"""Answer the question using only the context below.
    if the context doesn't contain the answer, say you don't know.
    Context:{context}
    Question:{question}
    Answer:
    """
    response = client.chat.completions.create(
        model = chat_model,
        messages = [{'role' : 'user' , 'content' : prompt}]
    )
    answer = response.choices[0].message.content
    if answer is None:
        raise RuntimeError("The chat completion returned no answer.")
    return answer

def main() -> None:
    documents = [
        """Project Helios Overview: Initiated in January 2024 by the municipal government of Neo-Veridia, Project Helios is an urban solar integration initiative designed to reduce the city's carbon footprint by 40% over five years. The project mandates that all commercial buildings exceeding three stories install high-efficiency photovoltaic (PV) glass windows by December 2026. Funded partially through a $45 million federal clean energy grant and municipal bonds, the program is overseen by Director Elena Rostova. Early pilot tests conducted in the downtown financial district showed a 28% decrease in grid electricity consumption for participating structures during the summer peak. However, supply chain delays for specialized silicon-perovskite cells pushed the initial rollout phase back by three months.
        """,
    ]
    store = build_index(documents)
    question = input("Enter your question")
    print(answer_question(question, store))


if __name__ == "__main__":
    main()