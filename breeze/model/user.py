# coding=utf8
from __future__ import print_function, division, absolute_import
import datetime
from sqlalchemy import Column, Integer, DateTime, String
from breeze.model import DBSession, ModelBase, BreezeModel
from sqlalchemy import func
from breeze.model import db_commit


class User(ModelBase, BreezeModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    password = Column(String(128))

