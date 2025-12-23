from models.models import User
from schemas.userschema import UserCreate, UserUpdate,UserResponse
# Asyncsession and select for database operations
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from utils.security import hashed_password

# Function to create a new user
async def create_user(db:AsyncSession,user:UserCreate)->UserResponse:
    new_user=User(
        name=user.name,
        email=user.email,
        image_url="htpps://cdn.oneewaee.com/krishna.jpg"
    )
    # pass hashing password function to hash the plain password
    new_user.hashed_password=hashed_password(user.password)
    db.add(new_user)
    try:
        await db.commit()
        await db.refresh(new_user)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email already registered")
    
    return new_user

