# coding=utf8

from __future__ import absolute_import, division, print_function

from flask import Blueprint
from breeze import auth
from breeze.api.handler import blog as blog_handler


blog_bp = Blueprint('blog', __name__, url_prefix='/blog')


@blog_bp.route('', methods=['POST'])
@auth.login_required
def save_blog():
    return blog_handler.save_blog()