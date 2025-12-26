from pydantic import BaseModel,EmailStr,Field,field_serializer
from typing import Optional
from config import settings

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

    @field_serializer("image_url")
    def serialize_image_url(self, image_url: Optional[str]) -> Optional[str]:
        if not image_url:
            return None
        return f"{settings.BASE_URL}{image_url}"

    class Config:
        orm_mode = True
    
# User update schema
class UserUpdate(BaseModel):
    name:Optional[str]
    email:Optional[EmailStr]
    phone:Optional[str]
    image_url:Optional[str]
    password:Optional[str]