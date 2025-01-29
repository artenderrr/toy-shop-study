from fastapi import FastAPI
from app.routers import toys, tags

app = FastAPI()

@app.get("/")
def hello() -> dict[str, str]:
    return {"message": "Hello World!"}

app.include_router(toys.router)
app.include_router(tags.router)