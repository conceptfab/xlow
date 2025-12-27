from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import uvicorn

app = FastAPI()

@app.get("/api/status")
def read_status():
    return {
        "message": "Cześć! To jest testowa aplikacja na Railway.",
        "platform": "Railway",
        "status": "Działa poprawnie",
        "env_var_test": os.getenv("RAILWAY_ENVIRONMENT", "Brak zmiennej środowiskowej (lokalnie?)")
    }

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
