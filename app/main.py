from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import include_routers

app = FastAPI(root_path="/api",
            title="Reminder App",
            version="1.0.0")

include_routers(app)

# Define who has access the the API endpoints by allowing specific CORS origins
origins: list[str] = [
    "http://localhost",
    "http://localhost:5173",
    "https://reminder-tasks-frontend.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=(origins),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
