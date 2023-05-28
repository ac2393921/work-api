from fastapi import FastAPI

from app.intarfaces.routers import works

app = FastAPI()
app.include_router(router=works.router)
