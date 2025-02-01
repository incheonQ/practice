from typing import Annotated
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from domain.question import question_router
import uvicorn

app = FastAPI()

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)

@app.get("/hello")
def hello():
    return {"message" : "안녕하세요!"}

@app.get("/parrot")
async def parrot(q: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
    if q:
        return {"q": q}
    return {"message": "쿼리 파라미터가 없습니다"}




# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="debug", access_log=True)