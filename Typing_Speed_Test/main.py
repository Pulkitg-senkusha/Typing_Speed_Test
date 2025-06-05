from fastapi import FastAPI
from api.routes import router
import uvicorn

app = FastAPI(title="Typing Speed API")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)