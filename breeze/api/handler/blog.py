# coding=utf8

from __future__ import absolute_import, division, print_function

from marshmallow.fields import Str
from breeze.model.blog import Blog
from breeze.utils.http import args_parser


def save_blog():
    blog_args = {
        'topic': Str(required=True),
        'genre': Str(required=True),
        'content': Str(required=True)
    }
    args = args_parser.parse(blog_args)
    topic = args.get('topic')
    genre = args.get('genre')
    content = args.get('content')
    Blog.add_blog(topic, genre, content)
    return {'msg': u'博客添加成功'}


