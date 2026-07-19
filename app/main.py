from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="Travel App API", version="0.1.0")
app.include_router(router)
