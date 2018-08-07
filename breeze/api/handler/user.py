# coding=utf8

from __future__ import absolute_import, division, print_function

from marshmallow.fields import Str
from flask_login import login_user, logout_user
from flask import g
from breeze.utils.http import args_parser
from breeze.model.user import User
from breeze.model import db_commit


def login():
    login_args = {
        'account': Str(required=True),
        'password': Str(required=True)
    }
    args = args_parser.parse(login_args)
    account = args.get('account')
    password = args.get('password')
    user = User.get(account)
    if user:
        verify = user.verify_password(password)
        if verify:
            login_user(user)
            g.user = user
            token = user.generate_auth_token()
            return {'code': 200, 'msg': u'登录成功', 'token': token}
    return {'code': 400, 'msg': u'账号或密码错误'}


def logout():
    logout_user()
    return {'code': 200, 'msg': u'注销成功'}


@db_commit
def register():
    register_args = {
        'account': Str(required=True),
        'password': Str(required=True)
    }
    args = args_parser.parse(register_args)
    account = args.get('account')
    password = args.get('password')
    user = User.get_account(account)
    if user:
        return {'code': 400, 'msg': u'账号已存在'}
    User.add(account, password)
    return {'code': 200, 'msg': u'账号注册成功'}
