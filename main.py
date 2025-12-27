from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Cześć! To jest testowa aplikacja na Railway.",
        "platform": "Railway",
        "status": "Działa poprawnie",
        "env_var_test": os.getenv("RAILWAY_ENVIRONMENT", "Brak zmiennej środowiskowej (lokalnie?)")
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
