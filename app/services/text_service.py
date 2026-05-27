import httpx
import requests
from app.config.settings import (
    settings
)


async def predict_text(text: str):
    """
    Call NLP model API
    """

    async with httpx.AsyncClient(
        timeout=settings.TEXT_API_TIMEOUT
    ) as client:

        response = await client.post(
            settings.TEXT_MODEL_API,

            json={
                "text": text
            }
        )

        response.raise_for_status()

        data = response.json()

        return data