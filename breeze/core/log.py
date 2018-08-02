# coding=utf8


def log_request(sender, **extra):
    sender.logger.info('Request start')


def log_response(sender, response, **extra):
    sender.logger.info('Response {}'.format(response.response))


def log_exception(sender, exception, **extra):
    sender.logger.error('Exception {}'.format(exception))

