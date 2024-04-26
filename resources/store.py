import os
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required

from db import db
from models import *
from rest_client import RestClient

blp = Blueprint("Store", __name__)

client = RestClient(os.getenv('STORE_API_URL'))

@blp.get("/rewards")
@jwt_required()
def get():
  rewards = client.get('rewards')

  return rewards