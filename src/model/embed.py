import ollama

import numpy as np


def text_to_embeddings(text: str) -> list:
    response = ollama.embed(model="all-minilm", input=text)

    embeddings = np.array(response["embeddings"])

    if embeddings.ndim == 2:
        embeddings = embeddings[0].tolist()

    return embeddings
