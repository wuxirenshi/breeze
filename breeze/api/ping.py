# coding=utf8

from __future__ import absolute_import, division, print_function

from flask import Blueprint
from marshmallow.fields import Str, Int
from breeze.utils.http import args_parser

ping_bp = Blueprint('ping', __name__)


@ping_bp.route('/ping', methods=['GET', 'POST'])
def ping():
    return 'pong'


@ping_bp.route('/ping/test')
def test_ping():
    test_args = {
        'name': Str(required=True),
        'password': Int(required=True)
    }
    args = args_parser.parse(test_args)
    return args
