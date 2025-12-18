# src/chunking/buffer_merger.py

def buffer_merge(sentences, buffer_size):
    """
    Buffer merging as described in SemRAG Algorithm 1
    """
    merged = []

    for i in range(len(sentences)):
        start = max(0, i - buffer_size)
        end = min(len(sentences), i + buffer_size + 1)
        merged.append(" ".join(sentences[start:end]))

    return merged
