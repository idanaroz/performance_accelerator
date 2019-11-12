# /app/__init__.py

import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)

    db.init_app(app) # bind database to flask app
    migrate.init_app(app, db)  # INITIALIZE MIGRATE
    # bootstrap.init_app()
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.catalog import main
    from app.auth import authentication

    app.register_blueprint(main)
    app.register_blueprint(authentication)

    return app



