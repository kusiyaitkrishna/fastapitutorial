from crud.user import create_user, get_users,upload_image, get_user_by_id, get_user_by_email,update_user
from models.models import User
from schemas.userschema import UserCreate, UserResponse,UserUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from db import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from fastapi import UploadFile, File

router = APIRouter(
    prefix="/users",
    tags=["User Management"]
)

@router.post("/",response_model=UserResponse)
async def register_user(user:UserCreate,db:AsyncSession=Depends(get_db)):
    """
    Endpoint to register a new user.
    """
    user = await create_user(db, user)
    return user

@router.post("/{user_id}/image",response_model=UserResponse)
async def upload_user_image(user_id:int,file:UploadFile=File(...),db:AsyncSession=Depends(get_db)):
    """
    Endpoint to upload a profile image for a user.
    """
    user = await upload_image(db,user_id,file)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user

@router.get("/",response_model=List[UserResponse])
async def list_users(skip:int=0,limit:int=10,db:AsyncSession=Depends(get_db)):
    """
    Endpoint to retrieve a list of users with pagination.
    """
    users = await get_users(db, skip, limit)
    return users

@router.get("/{user_id}",response_model=UserResponse)
async def get_user(user_id:int,db:AsyncSession=Depends(get_db)):
    """
    Endpoint to retrieve a user by their ID.
    """
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user

@router.get("/by-email/",response_model=UserResponse)
async def get_user_email(email:str,db:AsyncSession=Depends(get_db)):
    """
    Endpoint to retrieve a user by their email.
    """
    user = await get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user
@router.patch("/{user_id}",response_model=UserResponse)
async def update_user_info(user_id:int,user:UserUpdate,db:AsyncSession=Depends(get_db)):
    """
    Endpoint to update user information.
    """
    updated_user = await update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return updated_user

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