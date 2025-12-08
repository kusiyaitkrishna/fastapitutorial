from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    phone=Column(String,unique=True,nullable=True)

class Post(Base):
    __tablename__='posts'
    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    author=Column(String,nullable=False)
    
