from schemas.userschema import UserCreate, UserResponse, UserUpdate
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from db import get_db
from crud.user import create_user,get_users, get_user_by_email,update_user,delete_user

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

@router.put("/users/{email}",response_model=UserResponse)
async def update_existing_user(email:str,user_update:UserUpdate,db:AsyncSession=Depends(get_db)):
    updated_user=await update_user(db,email,user_update)
    return updated_user

@router.get("/users/{email}",response_model=UserResponse)
async def read_user_by_email(email:str,db:AsyncSession=Depends(get_db)):
    user=await get_user_by_email(db,email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.delete("/users/{email}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_by_email(email:str,db:AsyncSession=Depends(get_db)):
    success=await delete_user(db,email)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )