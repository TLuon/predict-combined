from typing import Dict
from typing import Any

from pydantic import BaseModel


class WeightSchema(
    BaseModel
):
    text: float
    image: float


class MetricSchema(
    BaseModel
):
    confidence: float
    entropy: float
    margin: float
    reliability: float


class PredictResponse(
    BaseModel
):
    prediction: str

    confidence: float

    weights: WeightSchema

    text_metrics: MetricSchema

    image_metrics: MetricSchema

    probabilities: Dict[
        str,
        float
    ]

    sources: Dict[
        str,
        Any
    ]