# coding=utf8

from __future__ import absolute_import, division, print_function

from flask import Blueprint
from breeze.model.user import User
from breeze.api.handler import user as user_handler
from breeze import auth


user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/login', methods=['POST'])
def login():
    return user_handler.login()


@user_bp.route('/logout', methods=['GET', 'POST'])
@auth.login_required
def logout():
    return user_handler.logout()


@user_bp.route('/register', methods=['POST'])
def register():
    return user_handler.register()


@user_bp.route('', methods=['GET'])
@auth.login_required
def user_info():
    return user_handler.get_user_info()


@auth.verify_token
def verify_token(token):
    return User.verify_auth_token(token)
