def normalize_weights(
    text_reliability: float,
    image_reliability: float
):
    """
    Normalize weights
    """

    total = (
        text_reliability +
        image_reliability
    )

    if total == 0:
        return 0.5, 0.5

    wt = text_reliability / total
    wi = image_reliability / total

    return (
        round(float(wt), 5),
        round(float(wi), 5)
    )