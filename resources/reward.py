import os
import json
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required
from flask import request

from db import db
from models import *
from rest_client import RestClient

blp = Blueprint("Reward", __name__)

client = RestClient(os.getenv('REWARDS_API_URL'))

@blp.get("/users/<int:user_id>/points")
@jwt_required()
def get_points(user_id):
  rewards = client.get(f"users/{user_id}/points")

  return rewards

@blp.post("/transactions")
@jwt_required()
def create_transaction():
  transaction_data = request.json

  response = client.post('transactions', transaction_data)

  return response