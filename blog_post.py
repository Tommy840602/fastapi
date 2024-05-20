from fastapi import APIRouter,Query, Path, Body
from pydantic import BaseModel
from typing import Optional
from typing import List

router = APIRouter(
    prefix="/blog",
    tags=["blogs"],
)

class BlogModel(BaseModel): 
    title:str
    content:str
    published:Optional[bool]
    comments_nums:int

@router.post('/new')
def create_blog(blog: BlogModel):
    return {"data":blog}

@router.post('/new/{id}')
def create_blog(blog: BlogModel,id: int,version: int=1):
    return {
        "id":id,
        "data":blog,
        "version":version
        }

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel,id: int,
                   comment_id: int=Query(None
                                         ,title="Comment ID的標題"
                                         ,description="Comment ID的一些說明"
                                         ,alias="commentId"
                                         ,deprecated=True),
    content: str = Body(..., min_length=12,max_length=24,regex="^[a-z\\s]*$"),
    version: Optional[List[str]] = Query(None)):           
    return {"blog": blog, "id": id, "comment_id": comment_id,"content":content,"version":version}

