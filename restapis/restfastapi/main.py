from fastapi import FastAPI
from .routers import itemrouter

app = FastAPI()
app.include_router(itemrouter)
