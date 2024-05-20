from fastapi import FastAPI
import blog_get
import blog_post

app = FastAPI()

# blog_get
app.include_router(blog_get.router)

# blog_post
app.include_router(blog_post.router)

@app.get("/")
def index():
    return {"Hello": "FastAPI"}

