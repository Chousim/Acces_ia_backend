from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.gemini_service import process_auditory_text

router = APIRouter(prefix="/api/v1/auditory", tags=["Modo Auditivo"])

class AuditoryRequest(BaseModel):
    raw_text: str

@router.post("/process")
def process_audio_text(request: AuditoryRequest):
    try:
        # Llamamos a Gemini para limpiar el texto y generar Smart Replies
        result = process_auditory_text(request.raw_text)
        return {
            "original_text": request.raw_text,
            "clean_text": result.get("clean_text", ""),
            "smart_replies": result.get("smart_replies", [])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar con Gemini: {str(e)}")

    except Exception as e:
        print(f"[ERROR AUDITIVO]: {repr(e)}", flush=True)
        raise HTTPException(status_code=500, detail=f"Error al procesar con Gemini: {str(e)}")