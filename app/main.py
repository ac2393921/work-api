from fastapi import FastAPI

from app.interfaces.routers import works

app = FastAPI()
app.include_router(router=works.router)
