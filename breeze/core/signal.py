from flask import (
    request_started,
    request_finished,
    got_request_exception,
    request
)

from breeze.core.log import (
    log_exception,
    log_request,
    log_response
)


def signal(app):
    request_started.connect(log_request, app)
    request_finished.connect(log_response, app)
    got_request_exception.connect(log_exception, app)
