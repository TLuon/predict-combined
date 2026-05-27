from typing import Optional

from pydantic import BaseModel


class PredictTextRequest(
    BaseModel
):
    text: str


class PredictCombinedRequest(
    BaseModel
):
    text: Optional[str] = None