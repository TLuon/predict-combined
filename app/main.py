from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from app.api.routes import router


app = FastAPI(
    title="Multimodal Fusion API",
    version="1.0.0"
)
# venv\Scripts\activate
# python training/train_model.py
# uvicorn app.main:app --reload
# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "*"
    ],

    allow_credentials=True,

    allow_methods=[
        "*"
    ],

    allow_headers=[
        "*"
    ]
)

# =========================
# Root
# =========================

@app.get("/")
async def root():

    return {
        "message":
            "Fusion API Running"
    }

# =========================
# Router
# =========================

app.include_router(router)