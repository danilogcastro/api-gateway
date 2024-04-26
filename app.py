from flask import Flask
from config import Config
from flask_smorest import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

import models

from db import db
from resources.user import blp as UserBlueprint
from resources.store import blp as StoreBlueprint
from resources.reward import blp as RewardBlueprint

def create_app(db_url=None):
  app = Flask(__name__)
  CORS(app)

  app.config.from_object(Config)
  app.config.from_envvar('APPLICATION_SETTINGS')

  db.init_app(app)

  migrate = Migrate(app, db)
  api = Api(app)
  jwt = JWTManager(app)

  api.register_blueprint(UserBlueprint)
  api.register_blueprint(StoreBlueprint)
  api.register_blueprint(RewardBlueprint)

  return app