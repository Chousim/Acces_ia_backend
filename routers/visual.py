from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional

router = APIRouter(prefix="/api/v1/visual", tags=["Modo Visual"])

@router.post("/analyze")
async def analyze_image(
    image: UploadFile = File(...),
    prompt: Optional[str] = Form(None)
):
    return {
        "filename": image.filename,
        "user_prompt": prompt or "Vistazo general del entorno",
        "description": "Respuesta de prueba para lectura en voz alta (TTS)"
    }