from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form
from fastapi import HTTPException

import asyncio

from app.services.text_service import (
    predict_text
)

from app.services.image_service import (
    predict_image
)

from app.services.fusion_service import (
    adaptive_fusion
)
from app.services.disease_service import (
    get_description
)

router = APIRouter()


@router.post("/predict-combined")
async def predict_combined(

    text: str = Form(None),

    image: UploadFile = File(None)
):
    """
    Unified multimodal endpoint
    """

    # =========================
    # Validate input
    # =========================

    if not text and not image:

        raise HTTPException(
            status_code=400,
            detail=(
                "Text or image required"
            )
        )

    # =========================
    # CASE 1
    # Text only
    # =========================

    if text and not image:

        text_result = await predict_text(
            text
        )

        return {
            "result": text_result
        }

    # =========================
    # CASE 2
    # Image only
    # =========================

    if image and not text:

        image_bytes = await image.read()

        image_result = await predict_image(
            image_bytes,
            image.filename
        )

        return {
            "result": image_result
        }

    # =========================
    # CASE 3
    # Text + Image
    # =========================

    image_bytes = await image.read()

    text_task = predict_text(
        text
    )

    image_task = predict_image(
        image_bytes,
        image.filename
    )

    text_result, image_result = (
        await asyncio.gather(
            text_task,
            image_task
        )
    )

    fusion_result = adaptive_fusion(
        text_result,
        image_result
    )

    return {

        "result": fusion_result
    }