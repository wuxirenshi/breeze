# coding=utf8

from breeze.api.ping import ping_bp
from breeze.api.user import user_bp
from breeze.api.blog import blog_bp
from breeze.exception.util import raise_user_exc
from breeze.exception.error_code import INVALID_ARGS

__all__ = [
    ping_bp,
    user_bp,
    blog_bp,
]


def api_init(app):
    for blue_print in __all__:
        app.register_blueprint(blue_print)

    @app.errorhandler(TypeError)
    def invalid_params(error):
        raise_user_exc(INVALID_ARGS)