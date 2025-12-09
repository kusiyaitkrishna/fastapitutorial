import pydantic
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name:str
    email:EmailStr
    phone:str|None=None

# Schema for updating user
class UserUpdate(BaseModel):
    name:str|None=None
    phone:str|None=None
class UserResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    phone:str|None=None

    class Config:
        orm_mode=True