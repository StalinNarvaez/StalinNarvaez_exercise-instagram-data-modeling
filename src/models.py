import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates = "follower")

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)

    follower = relationship("Follower", back_populates = "user")
    post = relationship("Post", back_populates = "user")
    comment = relationship("Comment", back_populates = "user")


    def to_dict(self):
        return {}

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))

    post = relationship("Post", back_populates = "media")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates = "post")
    media = relationship("Media", back_populates = "post")
    comment = relationship("Comment", back_populates = "post")


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    user = relationship("User", back_populates = "comment")
    post = relationship("Post", back_populates = "comment")

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
