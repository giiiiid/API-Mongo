from fastapi import APIRouter

run = APIRouter()

@run.get("/")
async def check_api():
    res = {
        "status": 200,
        "message": "API is running"
    }
    return res