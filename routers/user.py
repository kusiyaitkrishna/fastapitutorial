from crud.user import create_user
from models.models import User
from schemas.userschema import UserCreate, UserResponse
from sqlalchemy.ext.asyncio import AsyncSession
from db import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

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