from pydantic import BaseModel
from datetime import datetime


class CreatePostIn(BaseModel):
    gallery_id: int
    title: str
    content: str
    image_url: str

    class Config:
        schema_extra = {
            "example": {
                "gallery_id": 1,
                "title": "제목",
                "content": "내용",
                "image_url": "url",
            }
        }


class CreatePostOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Success to upload"}}


class UpdatePostIn(BaseModel):
    title: str
    content: str
    image_url: str

    class Config:
        schema_extra = {"example": {"title": "제목", "content": "내용", "image_url": "url"}}


class DeletePostOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Success to delete"}}


class UpdatePostOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Success to update"}}


class UploadImageOut(BaseModel):
    message: str
    image_url: str

    class Config:
        schema_extra = {
            "example": {
                "message": "Success to upload",
                "image_url": "https://gcinside.s3.ap-northeast-2.amazonaws.com/7.png",
            }
        }


class ReadPostOut(BaseModel):
    post_id: int
    author_id: int
    gallery_id: int
    post_title: str
    post_content: str
    post_image: str
    created_at: datetime
    like: int
    dislike: int

    class Config:
        schema_extra = {
            "example": {
                "post_id": "1",
                "author_id": "1",
                "gallery_id": "1",
                "post_title": "글제목",
                "post_content": "글내용",
                "post_image": "url",
                "created_at": "2022-06-28T00:49:39",
                "like": 0,
                "dislike": 0,
            }
        }


class LikePostOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Success to like post"}}


class DislikePostOut(BaseModel):
    message: str

    class Config:
        schema_extra = {"example": {"message": "Success to dislike post"}}


class ReadPostListOut(BaseModel):
    post_list: list

    class Config:
        schema_extra = {
            "example": {
                "post_list": [
                    {
                        "post_id": "1",
                        "author_id": "1",
                        "gallery_id": "1",
                        "post_title": "제목",
                        "post_content": "내용",
                        "post_image": "https://gcinside.s3.ap-northeast-2.amazonaws.com/7.png",
                        "created_at": "2020-01-01 00:00:00",
                        "like": "0",
                        "dislike": "0",
                    }
                ]
            }
        }


class ReadPopularPostListOut(BaseModel):
    popular_post_list: list

    class Config:
        schema_extra = {
            "example": {
                "popular_post_list": [
                    {
                        "post_id": "1",
                        "author_id": "1",
                        "gallery_id": "1",
                        "post_title": "제목",
                        "post_content": "내용",
                        "post_image": "https://gcinside.s3.ap-northeast-2.amazonaws.com/7.png",
                        "created_at": "2020-01-01 00:00:00",
                        "like": "0",
                        "dislike": "0",
                    }
                ]
            }
        }
