
from breeze.server import app
from flask_script import Manager
from breeze.model.user import User

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
