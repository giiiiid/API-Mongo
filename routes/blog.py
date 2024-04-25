from fastapi import APIRouter
from models.models import BlogModel
from config.config import blogs_collection
from serializer.serializer import decoded_data_list, decode_data
from bson import ObjectId
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


@blog.get("/blog/{blog_id}")
async def get_blog(blog_id: str):
    blog = blogs_collection.find_one( {"_id": ObjectId(blog_id) })
    decode_blog = decode_data(blog)

    return {
        "status": 200, 
        "data": decode_blog
    }


@blog.patch("/blog/update/{blog_id}")
async def update_blog(blog_id: str, blog: BlogModel):
    # if not blogs_collection.find_one({"_id" : ObjectId(blog_id)}):
    #     return {
    #         "status": 404,
    #         "message": "Blog does not exist"
    #     }
    updated_blog = dict(blog.model_dump())
    res = blogs_collection.find_one_and_update(
        {"_id": ObjectId(blog_id)},
        {"$set": updated_blog}
    )

    return {
        "status": 200,
        "message": "Blog has been successfully updated",
        "data": res
    }

@blog.delete("/blog/{blog_id}")
async def delete_blog(blog_id: str):
    blog = blogs_collection.find_one_and_delete( {"_id": ObjectId(blog_id)} )
    if blog is None:
        return {
            "status": 404,
            "message": "Blog does not exist"
        }
    return {
        "status": 201,
        "message": "Blog has been successfully deleted"
    }
      