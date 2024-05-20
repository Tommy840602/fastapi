from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum

router = APIRouter(
    prefix="/blog",
    tags=["blogs"],
)

# /blog/all
@router.get(
        "/all",
        summary="取得所有的 blogs",
        description="取得所有的 blogs，並且可以指定分頁的資料",
        response_description="所有的 blogs 資料"
        )
def get_blogs_all(page=1, page_size: Optional[int] = None):
    return {"message": f"所有的 blogs： 來自第 {page} 頁， 總共有 {page_size} 筆資料"}

# /blog/{id}/comments/{comment_id}
@router.get("/{id}/comments/{comment_id}", tags=["comments"])
def get_comment(
    id: int,
    comment_id: int,
    valid: bool = True,
    username: Optional[str] = None
      ):
    """
    取得 blog 的 comment 資料
    - **id**: blog 的 id
    - **comment_id**: comment 的 id
    - **valid**: comment 是否有效
    - **username**: 使用者名稱
    """
    return {"message": f"Blog 的 id 是：{id}， comment 的 id 是：{comment_id}， valid 是：{valid}"}

class BlogType(str, Enum):
    business = "business"
    story = "story"
    qa = "qa"

# /blog/type/{type}
@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog 的資料型態是 {type}"}

# /blog/{id}
@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"找不到 Blog 的 id ：{id}"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog 的 id 是：{id}"}
