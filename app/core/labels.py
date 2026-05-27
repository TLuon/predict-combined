"""
Unified labels across
all models
"""

LABEL_MAPPING = {

    # =====================
    # Acne
    # =====================

    "acne": "Acne",
    "Acne": "Acne",

    # =====================
    # Tinea
    # =====================

    "tinea": "Tinea",
    "Tinea": "Tinea",

    # =====================
    # Keratosis
    # =====================

    "keratosis": "Keratosis",
    "Keratosis": "Keratosis",

    "seborrh_keratoses":
        "Keratosis",

    "seborrheic_keratosis":
        "Keratosis",

    "Seborrh_Keratoses":
        "Keratosis",

    # =====================
    # Nevus
    # =====================

    "nevus": "Nevus",
    "Nevus": "Nevus",

    "moles": "Nevus",
    "Moles": "Nevus",

    # =====================
    # Unknown
    # =====================

    "unknown": "Unknown",
    "Unknown": "Unknown",

    "unknow": "Unknown",
    "UnKnow": "Unknown"
}


def normalize_label(label: str):
    """
    Normalize labels
    across all models
    """

    label = label.strip()

    return LABEL_MAPPING.get(
        label,
        label
    )