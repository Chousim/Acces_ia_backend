import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Cargamos las variables del archivo .env
load_dotenv()

# 2. Inicializamos el cliente de Gemini con la API Key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Definimos el modelo oficial habilitado en tu cuenta en una sola constante
MODEL_NAME = "gemini-3-flash-preview"

def process_auditory_text(raw_text: str) -> dict:
    """Limpia transcripciones con ruido/muletillas y genera Smart Replies."""
    prompt = f"""
    Eres un asistente de accesibilidad auditiva.
    Analiza el siguiente texto capturado por micrófono: "{raw_text}"
    1. Elimina muletillas, ruido y resúmelo en una frase directa y clara (clean_text).
    2. Genera entre 3 y 4 respuestas rápidas cortas (smart_replies) para que el usuario responda con un toque.
    Responde estrictamente en formato JSON con las llaves "clean_text" (string) y "smart_replies" (lista de strings).
    """
    
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        )
    )
    return json.loads(response.text)

def analyze_visual_image(image_bytes: bytes, mime_type: str, user_prompt: str = None) -> str:
    """Describe una imagen o responde una pregunta específica para usuarios con discapacidad visual."""
    instruccion = user_prompt if user_prompt else "Describe el entorno o lee el texto principal de esta imagen de forma clara, breve y directa."
    
    prompt_sistema = (
        f"Eres un asistente de accesibilidad visual. {instruccion} "
        "Sé conciso para que el lector de pantalla (TTS) lo lea rápido. "
        "Si algo no es legible con seguridad, indícalo claramente."
    )
    
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[
            types.Part.from_bytes(data=image_bytes, mime_type=mime_type),
            prompt_sistema
        ]
    )
    return response.text