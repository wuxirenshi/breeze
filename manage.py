
from breeze.server import app
from flask_script import Manager
from breeze.model.user import User
from breeze.model import ModelBase, engines

manager = Manager(app)


@manager.command
def create():
    ModelBase.metadata.create_all(engines['master'])


if __name__ == '__main__':
    manager.run()
