from flask import (
    request_started,
    request_finished,
    got_request_exception,
    request
)
from flask_login import user_logged_in, user_logged_out
from breeze.model import DBSession


def log_request(sender, **extra):
    sender.logger.info('Request start')


def log_response(sender, response, **extra):
    sender.logger.info('Response {}'.format(response.response))


def log_exception(sender, exception, **extra):
    sender.logger.error('Exception {}'.format(exception))


def track_login(sender, user, **extra):
    session = DBSession()
    user.active = True
    session.add(user)
    session.commit()


def track_logout(sender, user, **extra):
    session = DBSession()
    user.active = False
    session.add(user)
    session.commit()


def signal(app):
    request_started.connect(log_request, app)
    request_finished.connect(log_response, app)
    got_request_exception.connect(log_exception, app)
    user_logged_in(track_login, app)
    user_logged_out(track_logout, app)
