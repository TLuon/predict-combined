import httpx

from app.config.settings import (
    settings
)


async def predict_image(
    image_bytes,
    filename
):
    """
    Call Image model API
    """

    files = {
        "file": (
            filename,
            image_bytes,
            "image/jpeg"
        )
    }

    async with httpx.AsyncClient(
        timeout=settings.IMAGE_API_TIMEOUT
    ) as client:

        response = await client.post(
            settings.IMAGE_MODEL_API,
            files=files
        )

        response.raise_for_status()

        data = response.json()

        return data