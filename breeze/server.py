from breeze.core.app import BreezeApp
from flask_cors import CORS
from breeze.core.response import JSONResponse
from flask_login import LoginManager

from breeze import config

app = BreezeApp(__name__)
app.init(config)
app.response_class = JSONResponse
CORS(app)
login_manager = LoginManager(app)