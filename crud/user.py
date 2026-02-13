from models.models import User
from schemas.userschema import UserCreate, UserUpdate,UserResponse
# Asyncsession and select for database operations
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from utils.security import hashed_password
from utils.storage import save_upload_file

# Function to create a new user
async def create_user(db:AsyncSession,user:UserCreate)->UserResponse:
    new_user=User(
        name=user.name,
        email=user.email,
        image_url="https://cdn.oneewaee.com/krishna.jpg"
    )


    # pass hashing password function to hash the plain password
    hash_pwd=hashed_password(user.password)
    new_user.hashed_password=hash_pwd
    db.add(new_user)
    try:
        await db.commit()
        await db.refresh(new_user)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email already registered")
    
    return new_user


# Function to upload user image
async def upload_image(db:AsyncSession,user_id:int,file):
    result =await db.execute(select(User).where(User.id==user_id))
    user=result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    # Save image
    user.image_url=await save_upload_file(file,subdir="users")
    await db.commit()
    await db.refresh(user)
    return user

#method to get list of user
async def get_users(db:AsyncSession,skip:int=0,limit:int=10)->List[UserResponse]:
    result=await db.execute(select(User).offset(skip).limit(limit))
    users=result.scalars().all()
    return users

# method to get user by id
async def get_user_by_id(db:AsyncSession,user_id:int)->Optional[UserResponse]:
    result=await db.execute(select(User).where(User.id==user_id))
    user=result.scalar_one_or_none()
    return user

# get user by email
async def get_user_by_email(db:AsyncSession,email:str)->Optional[UserResponse]:
    result=await db.execute(select(User).where(User.email==email))
    user=result.scalar_one_or_none()
    return user

# function to update user data
async def update_user(db:AsyncSession,user_id:int,user_update:UserUpdate)->Optional[UserResponse]:
    user=await get_user_by_id(db,user_id)
    if not user:
        return None

    for var, value in vars(user_update).items():
        if value is not None:
            setattr(user, var, value)
    
    
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user