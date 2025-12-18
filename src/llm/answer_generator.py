# src/llm/answer_generator.py

import ollama


def generate_answer(context_chunks, question):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are an expert assistant answering questions based on Dr. B. R. Ambedkar's writings.

Context:
{context}

Question:
{question}

Answer clearly and factually.
"""

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
