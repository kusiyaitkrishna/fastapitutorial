from db import Base
from sqlalchemy import Column, ForeignKey, DateTime, Boolean, String, Enum, Index, Integer
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from datetime import datetime



# User models for cms system
class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    phone=Column(String,unique=True,nullable=True)
    hashed_password=Column(String,nullable=False)
    image_url=Column(String,nullable=True)
    posts=relationship('Post',back_populates='author')
    comments=relationship('Comment',back_populates='user')
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
 # Category models for cms system
class Category(Base):
    __tablename__='categories'
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    description=Column(String,nullable=True)
    image_url =Column(String,nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    posts=relationship('Post',back_populates='category')


# Tags models for cms system
class Tag(Base):
    __tablename__='tags'
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    description=Column(String,nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    posts=relationship('Post',secondary='post_tags',back_populates='tags')


class Post(Base):
    __tablename__='posts'
    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False)
    description=Column(String,nullable=True)
    content=Column(String,nullable=False)
    image_url=Column(String,nullable=True)
    author_id=Column(Integer,ForeignKey('users.id'),nullable=False)
    category_id=Column(Integer,ForeignKey('categories.id'),nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author=relationship('User',back_populates='posts')
    category=relationship('Category',back_populates='posts')
    comments=relationship('Comment',back_populates='post')
    tags=relationship('Tag',secondary='post_tags',back_populates='posts')

class Comment(Base):
    __tablename__='comments'
    id=Column(Integer,primary_key=True)
    post_id=Column(Integer,ForeignKey('posts.id'),nullable=False)
    user_id=Column(Integer,ForeignKey('users.id'),nullable=False)
    message=Column(String,nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    post=relationship('Post',back_populates='comments')
    user=relationship('User',back_populates='comments')


# Association table for many-to-many relationship between Post and Tag
post_tags=Table(
    'post_tags',
    Base.metadata,
    Column('post_id',Integer,ForeignKey('posts.id'),primary_key=True),
    Column('tag_id',Integer,ForeignKey('tags.id'),primary_key=True)
)







    
