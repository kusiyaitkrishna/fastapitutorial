from schemas.userschema import UserCreate,UserResponse
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