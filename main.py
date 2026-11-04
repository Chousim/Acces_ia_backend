from fastapi import FastAPI

# 1. Creamos la instancia principal de nuestra API
app = FastAPI(
    title="AccessIA Backend",
    description="Microservicio intermediario entre Flutter y Google Gemini API",
    version="0.1.0"
)

# 2. Definimos un endpoint GET en la ruta raíz ("/")
@app.get("/")
def health_check():
    return {
        "status": "online",
        "service": "AccessIA Backend",
        "message": "Hola Mundo, el servidor está funcionando"
    }