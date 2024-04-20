from fastapi import FastAPI
from routes.run import run
from routes.blog import blog


app = FastAPI()


app.include_router(run)
app.include_router(blog)