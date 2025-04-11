from fastapi import FastAPI
from app.routes import home, upload, predict, database
from google.cloud import storage
import os
import uvicorn

app = FastAPI(title="StressXOR")

# Inicializar el cliente de Google Cloud Storage sin credenciales manuales
storage_client = storage.Client()

# Incluir routers (endpoints) definidos en cada módulo de routes
app.include_router(home.router)
app.include_router(upload.router)
app.include_router(predict.router)
app.include_router(database.router)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Usar 8080 como predeterminado solo para pruebas locales
    uvicorn.run("main:app", host="0.0.0.0", port=port)