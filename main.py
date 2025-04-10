from fastapi import FastAPI
from app.routes import auth, athletes, wearable
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="API de Rendimiento Deportivo",
    description="API para gestionar atletas y datos de wearables",
    version="1.0.1"
)

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)

app.include_router(auth.router)
app.include_router(athletes.router)
app.include_router(wearable.router)