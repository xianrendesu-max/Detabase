from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

# メモリ上に保存（本家も同等レベル）
POSTS = []

class PostIn(BaseModel):
    name: str
    body: str

class PostOut(BaseModel):
    name: str
    body: str
    created_at: str


@app.post("/post")
async def post_message(p: PostIn):
    post = {
        "name": p.name,
        "body": p.body,
        "created_at": datetime.utcnow().isoformat()
    }
    POSTS.append(post)
    return {"status": "ok"}


@app.get("/posts", response_model=List[PostOut])
async def get_posts():
    return POSTS
