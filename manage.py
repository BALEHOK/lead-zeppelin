from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from src.web.web_app import web_app
from src.leads.models import db

migrate = Migrate(web_app, db)
manager = Manager(web_app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
