# coding=utf8

from __future__ import absolute_import, division, print_function

from marshmallow.fields import Str
from flask_login import login_user, logout_user
from breeze.utils.http import args_parser
from breeze.model.user import User


def login():
    login_args = {
        'account': Str(required=True),
        'password': Str(required=True)
    }
    args = args_parser.parse(login_args)
    account = args.get('account')
    password = args.get('password')
    user = User.get(account, password)
    if user:
        login_user(user)
        return {'code': 200, 'msg': u'登录成功'}
    return {'code': 200, 'msg': u'用户不存在，请注册'}


def logout():
    logout_user()
    return {'code': 200, 'msg': u'注销成功'}


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
        return {'code': 200, 'msg': u'账号已存在'}
    User.add(account, password)
    return {'code': 200, 'msg': u'账号注册成功'}
