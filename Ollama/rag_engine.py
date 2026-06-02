import ollama

# Load dataset
dataset = []

with open("cat-facts.txt", "r", encoding="utf-8") as file:
    dataset = file.readlines()

print(f"Loaded {len(dataset)} entries")

# Models
EMBEDDING_MODEL = "hf.co/CompendiumLabs/bge-base-en-v1.5-gguf"
LANGUAGE_MODEL = "hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF"

VECTOR_DB = []

def add_chunk_to_database(chunk):
    embedding = ollama.embed(
        model=EMBEDDING_MODEL,
        input=chunk
    )["embeddings"][0]

    VECTOR_DB.append((chunk, embedding))

# Build vector database
for i, chunk in enumerate(dataset):
    add_chunk_to_database(chunk)
    print(f"Added chunk {i+1}/{len(dataset)}")


def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x ** 2 for x in a) ** 0.5
    norm_b = sum(x ** 2 for x in b) ** 0.5

    if norm_a == 0 or norm_b == 0:
        return 0

    return dot_product / (norm_a * norm_b)


def retrieve(query, top_n=3):
    query_embedding = ollama.embed(
        model=EMBEDDING_MODEL,
        input=query
    )["embeddings"][0]

    similarities = []

    for chunk, embedding in VECTOR_DB:
        similarity = cosine_similarity(
            query_embedding,
            embedding
        )

        similarities.append(
            (chunk, similarity)
        )

    similarities.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return similarities[:top_n]


def generate_response(query):

    retrieved = retrieve(query)

    context = "\n".join(
        [chunk for chunk, _ in retrieved]
    )

    prompt = f"""
You are a helpful chatbot.

Use ONLY the following context:

{context}
"""

    response = ollama.chat(
        model=LANGUAGE_MODEL,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return response["message"]["content"]