import sys

from flask import Flask
from breeze.api import api_init
from breeze.core.signal import signal

reload(sys)
sys.setdefaultencoding('utf-8')


class BreezeApp(Flask):

    def init(self, settings):
        self.config.update(**settings.FLASK)
        api_init(self)
        signal(self)
