from app.utils.entropy import (
    calculate_entropy
)

from app.utils.margin import (
    calculate_margin
)


def calculate_reliability(result: dict):
    """
    Reliability score

    R = confidence × (1 - entropy) × margin
    """

    confidence = result.get(
        "confidence",
        0
    )

    probabilities = result.get(
        "probabilities",
        {}
    )

    entropy = calculate_entropy(
        probabilities
    )

    margin = calculate_margin(
        probabilities
    )

    reliability = (
        confidence *
        (1 - entropy) *
        margin
    )

    return {
        "confidence": round(confidence, 5),

        "entropy": round(entropy, 5),

        "margin": round(margin, 5),

        "reliability": round(
            float(reliability),
            5
        )
    }