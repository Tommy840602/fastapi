from fastapi import APIRouter,Query, Path, Body
from pydantic import BaseModel
from typing import Optional
from typing import List
from typing import Dict

router = APIRouter(
    prefix="/blog",
    tags=["blogs"],
)

class Image(BaseModel):
    url:str
    alias:str

class BlogModel(BaseModel): 
    title:str
    content:str
    published:Optional[bool]
    nb_comments:int
    tags:List[str]=[]
    metadata: Dict[str, str] = {"key1": "value1"}
    image: Optional[Image] = None    

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

@router.post("/new/{id}/comment/{comment_id}")
def create_comment(
    blog: BlogModel, id: int,
    comment_title: int = Query(None,
                               title="Comment Title的標題",
                               description="Comment Title的一些說明", alias="commentTitle",
                               deprecated=True,
                               ),
    content: str = Body(..., min_length=10, max_length=50, regex='^[a-z\\s]*$'),
    version: Optional[List[str]] = Query(['1.0', '1,5', '2.0']),
    comment_id: int = Path(..., le=5)
    ):

    return {
            "blog": blog,
            "id": id,
            "comment_title": comment_title,
            "content": content,
            "version": version,
            "comment_id": comment_id
            }

