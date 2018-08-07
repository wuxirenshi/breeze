# coding=utf8
from __future__ import print_function, division, absolute_import
import datetime
from sqlalchemy import Column, Integer, DateTime, String, Boolean, Table, ForeignKey
from breeze.model import DBSession, ModelBase, BreezeModel
from sqlalchemy import func
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin
from breeze.model import db_commit


class User(ModelBase, BreezeModel, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    account = Column(String(128), unique=True)
    password = Column(String(128))
    active = Column(Boolean)
    register_at = Column(DateTime, default=datetime.datetime.now)

    @classmethod
    def get(cls, account, password):
        return DBSession().query(cls).filter(cls.account == account, cls.password == password).first()

    @classmethod
    def get_account(cls, account):
        return DBSession().query(cls).filter(cls.account == account).first()

    @classmethod
    def add(cls, account, password):
        session = DBSession()
        user = cls(account=account, password=password, active=False)
        session.add(user)
        session.flush()

