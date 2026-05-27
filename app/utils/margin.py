def calculate_margin(probabilities: dict):
    """
    Margin = top1 - top2

    Larger margin = more confident
    """

    probs = sorted(
        probabilities.values(),
        reverse=True
    )

    if len(probs) < 2:
        return 0.0

    margin = probs[0] - probs[1]

    return round(float(margin), 5)