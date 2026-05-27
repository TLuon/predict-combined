import numpy as np


def calculate_entropy(probabilities: dict):
    """
    Calculate normalized entropy

    Lower entropy = higher confidence
    """

    probs = np.array(
        list(probabilities.values())
    )

    epsilon = 1e-10

    entropy = -np.sum(
        probs * np.log(probs + epsilon)
    )

    max_entropy = np.log(len(probs))

    normalized_entropy = entropy / max_entropy

    return round(
        float(normalized_entropy),
        5
    )