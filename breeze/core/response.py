# coding=utf8

from werkzeug.wrappers import Response
from flask import jsonify


class JSONResponse(Response):
    _header_dict = {'Content-Type': 'application/json'}

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)
        h = response.headers
        for header, value in cls._header_dict.items():
            h[header] = value
        return super(JSONResponse, cls).force_type(response, environ)
