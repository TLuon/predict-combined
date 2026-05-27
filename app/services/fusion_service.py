from app.services.reliability_service import (
    calculate_reliability
)

from app.services.disease_service import (
    get_description
)

from app.utils.normalization import (
    normalize_weights
)

from app.core.labels import (
    normalize_label
)


def normalize_probabilities(
    probabilities: dict
):
    """
    Normalize labels
    before fusion
    """

    normalized = {}

    for label, prob in probabilities.items():

        new_label = normalize_label(
            label
        )

        normalized[new_label] = (

            normalized.get(
                new_label,
                0
            )

            + prob
        )

    return normalized


def adaptive_fusion(
    text_result: dict,
    image_result: dict
):
    """
    Dynamic multimodal fusion
    """

    # =========================
    # Reliability
    # =========================

    text_metrics = calculate_reliability(
        text_result
    )

    image_metrics = calculate_reliability(
        image_result
    )

    Rt = text_metrics[
        "reliability"
    ]

    Ri = image_metrics[
        "reliability"
    ]

    # =========================
    # Dynamic weights
    # =========================

    wt, wi = normalize_weights(
        Rt,
        Ri
    )

    # =========================
    # Normalize probabilities
    # =========================

    text_probs = normalize_probabilities(

        text_result.get(
            "probabilities",
            {}
        )
    )

    image_probs = normalize_probabilities(

        image_result.get(
            "probabilities",
            {}
        )
    )

    # =========================
    # Unified classes
    # =========================

    all_classes = {

        "Acne",

        "Tinea",

        "Keratosis",

        "Nevus",

        "Unknown"
    }

    final_probs = {}

    # =========================
    # Fusion
    # =========================

    for cls in all_classes:

        pt = text_probs.get(
            cls,
            0
        )

        pi = image_probs.get(
            cls,
            0
        )

        final_probs[cls] = round(

            (wt * pt)

            +

            (wi * pi),

            5
        )

    # =========================
    # Final prediction
    # =========================

    prediction = max(
        final_probs,
        key=final_probs.get
    )

    confidence = final_probs[
        prediction
    ]

    # =========================
    # Get description from SQL
    # =========================

    description = get_description(
        prediction
    )

    # =========================
    # Final response
    # =========================

    return {

        "prediction": prediction,

        "confidence": round(
            float(confidence),
            5
        ),

        "weights": {

            "text": round(
                wt,
                5
            ),

            "image": round(
                wi,
                5
            )
        },

        "description": description
    }