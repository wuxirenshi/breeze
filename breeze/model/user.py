# coding=utf8
from __future__ import print_function, division, absolute_import
import datetime
from sqlalchemy import Column, Integer, DateTime, String, Boolean, Table, ForeignKey, SmallInteger
from breeze.model import DBSession, ModelBase, BreezeModel
from sqlalchemy import func
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin
from breeze.config import SECRET_KEY
from . import db_commit
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import (
    TimedJSONWebSignatureSerializer,
    SignatureExpired,
    BadSignature
)


class User(ModelBase, BreezeModel, UserMixin):
    __tablename__ = 'user'

    ADMIN = 2
    HR = 1

    id = Column(Integer, primary_key=True)
    account = Column(String(128), unique=True)
    password_hash = Column(String(128))
    token = Column(String(128))
    role = Column(SmallInteger, default=HR)
    active = Column(Boolean)
    register_at = Column(DateTime, default=datetime.datetime.now)

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration=6000):
        s = TimedJSONWebSignatureSerializer(SECRET_KEY, expires_in=expiration)
        return s.dumps((self.id, self.account, self.role, self.active))

    @classmethod
    def get_user_by_id(cls, user_id):
        return DBSession().query(cls).filter(cls.id == user_id).first()

    @classmethod
    def get_user_by_token(cls, token):
        s = TimedJSONWebSignatureSerializer(SECRET_KEY)
        try:
            user_id, account, role, active = s.loads(token)
        except SignatureExpired:
            return False
        except BadSignature:
            return False
        user = User.get_user_by_id(user_id)
        return user

    @staticmethod
    def verify_auth_token(token):
        s = TimedJSONWebSignatureSerializer(SECRET_KEY)
        try:
            user_id, account, role, active = s.loads(token)
        except SignatureExpired:
            return False
        except BadSignature:
            return False
        user = User.get_user_by_id(user_id)
        if user:
            return True
        return False

    @classmethod
    def get(cls, account):
        return DBSession().query(cls).filter(cls.account == account).first()

    @classmethod
    def get_account(cls, account):
        return DBSession().query(cls).filter(cls.account == account).first()

    @classmethod
    @db_commit
    def add(cls, account, password):
        session = DBSession()
        user = cls(account=account, active=False)
        user.hash_password(password)
        session.add(user)
        session.flush()
