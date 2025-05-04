"""Flask app initialization."""

import logging
import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db_url = os.getenv('DATABASE_URL', 'postgresql://myuser:mypass@localhost/mydb')

db = SQLAlchemy()
migrate = Migrate()


def create_app() -> Flask:
  """Create the Flask app."""

  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = db_url
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['SQLALCHEMY_ECHO'] = (
      os.getenv('FLASK_SERVER_ENV', 'development') == 'development'
  )

  # Set the logging level based on the environment.
  log_level = (
      logging.DEBUG
      if os.getenv('FLASK_SERVER_ENV', 'development') == 'development'
      else logging.INFO
  )
  app.logger.setLevel(log_level)

  # Initialize the database and migration tool.
  db.init_app(app)
  migrate.init_app(app, db)

  # Register the API blueprint.
  from .routes import api_bp

  app.register_blueprint(api_bp)
  app.logger.info('Flask app created.')

  return app
