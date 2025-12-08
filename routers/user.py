from schemas.userschema import UserCreate, UserResponse
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from db import get_db
from crud.user import create_user,get_users

router =APIRouter(
    tags=["users"]
)

@router.post("/users",response_model=UserResponse)
async def create_new_user(user:UserCreate,db:AsyncSession=Depends(get_db)):
    try:
        new_user=await create_user(db,user)
        return new_user
    except ValueError as ve:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ve)
        )

@router.get("/users",response_model=list[UserResponse])
async def read_users(db:AsyncSession=Depends(get_db)):
    users=await get_users(db)
    return users