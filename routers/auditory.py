from fastapi import APIRouter
from pydantic import BaseModel

# 1. Creamos un agrupador de rutas para el modo auditivo
router = APIRouter(prefix="/api/v1/auditory", tags=["Modo Auditivo"])

# 2. Definimos qué datos esperamos recibir de Flutter (el texto crudo del micrófono)
class AuditoryRequest(BaseModel):
    raw_text: str

# 3. Endpoint POST que devolverá el texto limpio y las Smart Replies
@router.post("/process")
def process_audio_text(request: AuditoryRequest):
    return {
        "original_text": request.raw_text,
        "clean_text": "Texto de prueba limpio sin muletillas",
        "smart_replies": ["Sí, por favor", "No, gracias", "Para llevar"]
    }