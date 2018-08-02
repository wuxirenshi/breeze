from breeze.api.ping import ping_bp

__all__ = [
    ping_bp,
]


def api_init(app):
    for blue_print in __all__:
        app.register_blueprint(blue_print)
