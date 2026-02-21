from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(min_length=1, max_length=120)

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=50)

class UserPrivate(BaseModel):
    email: EmailStr = Field(min_length=1, max_length=120)

class UserPublic(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    image_file: str | None
    image_path: str


class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=100)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    date_posted: datetime
    author: UserPublic
    

class PostUpdate(PostBase):
    pass

class PostUpdatePartial(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    content: str | None = Field(default=None, min_length=1, max_length=100)

class Token(BaseModel):
    access_token: str 
    token_type : str