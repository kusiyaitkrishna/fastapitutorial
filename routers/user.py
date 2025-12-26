from crud.user import create_user,upload_image
from models.models import User
from schemas.userschema import UserCreate, UserResponse
from sqlalchemy.ext.asyncio import AsyncSession
from db import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from fastapi import UploadFile, File

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/",response_model=UserResponse)
async def register_user(user:UserCreate,db:AsyncSession=Depends(get_db)):
    """
    Endpoint to register a new user.
    """
    db_user = await create_user(db, user)
    return db_user

@router.post("/{user_id}/image",response_model=UserResponse)
async def upload_user_image(user_id:int,file:UploadFile=File(...),db:AsyncSession=Depends(get_db)):
    """
    Endpoint to upload a profile image for a user.
    """
    user = await upload_image(db,user_id,file)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user


# @router.post(
#     "/{user_id}/image",
#     response_model=UserResponse
# )
# async def upload_user_profile_image(
#     user_id: int,
#     file: UploadFile = File(...),
#     db: AsyncSession = Depends(get_db),
# ):
#     """
#     Upload profile image for a user
#     """
#     user = await upload_user_image(db, user_id, file)
#     return user