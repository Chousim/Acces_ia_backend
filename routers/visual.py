from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
from services.gemini_service import analyze_visual_image

router = APIRouter(prefix="/api/v1/visual", tags=["Modo Visual"])

@router.post("/analyze")
async def analyze_image(
    image: UploadFile = File(...),
    prompt: Optional[str] = Form(None)
):
    try:
        # 1. Leemos los bytes de la foto subida desde el celular
        image_bytes = await image.read()
        mime_type = image.content_type or "image/jpeg"
        
        # 2. Enviamos la imagen y la pregunta (si existe) a Gemini
        description = analyze_visual_image(image_bytes, mime_type, prompt)
        
        return {
            "filename": image.filename,
            "user_prompt": prompt or "Vistazo general del entorno",
            "description": description
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al analizar imagen con Gemini: {str(e)}")