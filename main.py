from fastapi import FastAPI
from routers import visual, auditory

app = FastAPI(
    title="AccessIA Backend",
    description="Microservicio intermediario entre Flutter y Google Gemini API",
    version="0.1.0"
)

# Conectamos las rutas visuales y auditivas a la aplicación principal
app.include_router(visual.router)
app.include_router(auditory.router)

@app.get("/")
def health_check():
    return {
        "status": "online",
        "service": "AccessIA Backend",
        "message": "Hola Mundo, el servidor está funcionando"
    }