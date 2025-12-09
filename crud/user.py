from schemas.userschema import UserCreate,UserResponse,UserUpdate
from models.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

# Function to create new user
async def create_user(db:AsyncSession,user:UserCreate)->UserResponse:
    # Creating new user instance or object
    new_user=User(name=user.name,email=user.email,phone=user.phone)
    # Adding the new user to the session
    db.add(new_user)

    try:
        # Committing the session to save the new user to the database
        await db.commit()

        await db.refresh(new_user)
        return new_user

    except IntegrityError:
        await db.rollback()
        raise ValueError("User with this email or phone already exists.")
    

# Function to read list of the users
async def get_users(db:AsyncSession)->list[UserResponse]:
    result=await db.execute(select(User))
    users=result.scalars().all()
    return users

# Function to read single user by email
async def get_user_by_email(db:AsyncSession,email:str)->UserResponse|None:
    result =await db.execute(select(User).where(User.email==email))
    user=result.scalars().first()
    return user

# Function to update userdata
async def update_user(db:AsyncSession,email:str,user_update:UserUpdate)->UserResponse|None:
    user=await get_user_by_email(db,email=email)
    if not user:
        return None
    if user_update.name is not None:
        user.name=user_update.name
    if user_update.phone is not None:
        user.phone=user_update.phone
    try:
        await db.commit()
        await db.refresh(user)
        return user
    except IntegrityError:
        await db.rollback()
        raise ValueError("Phone number already exists.")

# Function to delete user by email
async def delete_user(db:AsyncSession,email:str)->bool:
    user=await get_user_by_email(db,email=email)
    if not user:
        return False
    await db.delete(user)
    await db.commit()
    return True