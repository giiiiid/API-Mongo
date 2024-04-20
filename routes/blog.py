from fastapi import APIRouter
from models.models import BlogModel


blog = APIRouter()


# endpoints
@blog.post("/blog/create", response_model=BlogModel)
async def create_blog(blog:BlogModel):
    new_blog = blog.model_dump()
    return new_blog