# src/chunking/semantic_chunker.py

import pdfplumber
import nltk
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from .buffer_merger import buffer_merge

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)


MODEL_NAME = "all-MiniLM-L6-v2"


def extract_sentences_from_pdf(pdf_path):
    sentences = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                sentences.extend(nltk.sent_tokenize(text))
    return sentences


def semantic_chunking(
    pdf_path,
    buffer_size=3,
    similarity_threshold=0.75,
    max_sentences_per_chunk=8
):
    """
    Improved SemRAG-style semantic chunking
    """
    model = SentenceTransformer(MODEL_NAME)

    sentences = extract_sentences_from_pdf(pdf_path)
    buffered = buffer_merge(sentences, buffer_size)
    embeddings = model.encode(buffered)

    chunks = []
    current_chunk = []

    for i in range(len(buffered) - 1):
        sim = cosine_similarity(
            [embeddings[i]], [embeddings[i + 1]]
        )[0][0]

        current_chunk.append(sentences[i])

        # Split condition (semantic OR size-based)
        if (
            sim < similarity_threshold
            or len(current_chunk) >= max_sentences_per_chunk
        ):
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return sentences, chunks
