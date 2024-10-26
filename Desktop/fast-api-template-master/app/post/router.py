from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.post.models import Post
from app.post.schemas import SSPost

router = APIRouter(prefix="/post", tags=["post"])



@router.post("/set-post")
async def set_post(data:SSPost):
    await Post.create(
        title=data.title,
        content=data.content,
    )
    return {
        "status": "success",
    }


@router.get("/get-post")
async def get_post():
    posts = await Post.get_all()

    return {
        'result':posts
    }


@router.delete("/delete-post/{post_id}")
async def delete_post(post_id:int):

    await Post.delete(Post.id == post_id)

    return {
        'status': 'success',
    }




@router.patch('/update-post/{post_id}')
async def update_post(post_id:int, data:SSPost):
    post = await Post.find_by_id(post_id)
    await Post.update(model_id=post.id, title=data.title, content=data.content)
    return {
        'status': 'success',
    }