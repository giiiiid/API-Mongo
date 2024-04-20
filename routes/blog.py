from fastapi import APIRouter
from models.models import BlogModel
from config.config import blogs_collection
from serializer.serializer import decoded_data_list
import  datetime


blog = APIRouter()


# endpoints
@blog.post("/blog/create")
async def create_blog(blog:BlogModel):
    new_blog = blog.model_dump()
    current_date = datetime.date.today()
    new_blog["date"] = str(current_date)

    res = blogs_collection.insert_one(new_blog)

    return {
        "status": 201,
        "message": "New blog created!",
        "id": str(res.inserted_id)
    }


@blog.get("/blogs/all")
async def all_blogs():
    blogs = blogs_collection.find()
    return {
        "status": 200,
        "data": decoded_data_list(blogs)
    }