# coding=utf8

from __future__ import absolute_import, division, print_function

from flask import Blueprint
from flask_login import login_required
from breeze.api.handler import user as user_handler

user_bp = Blueprint('user', __name__, url_prefix='user')


@user_bp.route('/login', method=['GET'])
def login():
    return user_handler.login()


@user_bp.route('/logout', method=['POST'])
@login_required
def logout():
    return user_handler.logout()


@user_bp.route('/register', method=['POST'])
def register():
    return user_handler.register()

