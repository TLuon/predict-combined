import numpy as np


def cosine_similarity(vec1, vec2):
    """
    Cosine similarity

    Range:
    -1 -> opposite
    0 -> unrelated
    1 -> identical
    """

    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    dot_product = np.dot(vec1, vec2)

    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)

    if norm_a == 0 or norm_b == 0:
        return 0.0

    similarity = dot_product / (norm_a * norm_b)

    return round(float(similarity), 5)
