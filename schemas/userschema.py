from pydantic import BaseModel,EmailStr,Field
from typing import Optional

# User create schema
class UserCreate(BaseModel):
    name:str
    email:EmailStr
    password:str

# User response schema
class UserResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    phone:Optional[str]
    image_url:Optional[str]

    class Config:
        orm_mode = True
    
# User update schema
class UserUpdate(BaseModel):
    name:Optional[str]
    email:Optional[EmailStr]
    phone:Optional[str]
    image_url:Optional[str]
    password:Optional[str]