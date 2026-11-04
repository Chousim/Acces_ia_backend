from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
from services.gemini_service import analyze_visual_image

router = APIRouter(prefix="/api/v1/visual", tags=["Modo Visual"])

@router.post("/analyze")
def analyze_image(
    image: UploadFile = File(...),
    prompt: Optional[str] = Form(None)
):
    try:
        # Lectura síncrona para que FastAPI la ejecute en un hilo separado (threadpool)
        image_bytes = image.file.read()
        
        # Si Flutter envía application/octet-stream, asignamos image/jpeg por defecto
        mime_type = image.content_type
        if not mime_type or not mime_type.startswith("image/"):
            mime_type = "image/jpeg"
        
        description = analyze_visual_image(image_bytes, mime_type, prompt)
        
        return {
            "filename": image.filename,
            "user_prompt": prompt or "Vistazo general del entorno",
            "description": description
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al analizar imagen con Gemini: {str(e)}")

    except Exception as e:
        print(f"[ERROR VISUAL]: {repr(e)}", flush=True)
        raise HTTPException(status_code=500, detail=f"Error al analizar imagen con Gemini: {str(e)}")