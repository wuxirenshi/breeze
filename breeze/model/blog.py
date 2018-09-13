# coding=utf8
from __future__ import print_function, division, absolute_import
import datetime
from sqlalchemy import Column, Integer, DateTime, String, Text, Boolean, Table, ForeignKey, SmallInteger
from breeze.model import DBSession, ModelBase, BreezeModel
from sqlalchemy import func
from . import db_commit
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin


class Blog(ModelBase, BreezeModel, UserMixin):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    topic = Column(String(128), unique=True)
    genre = Column(String(128))
    content = Column(Text, default='')
    
    @classmethod
    @db_commit
    def add_blog(cls, topic, genre, content):
        session = DBSession()
        blog = cls(topic=topic, genre=genre, content=content)
        session.add(blog)
        session.flush()