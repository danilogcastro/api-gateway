from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from passlib.hash import pbkdf2_sha256

from db import db
from models import User
from schemas import UserSchema

blp = Blueprint("Users", __name__)

@blp.post("/users")
@blp.arguments(UserSchema)
@blp.response(201, UserSchema)
def create(user_data):
  if User.query.filter(User.username == user_data["username"]).first():
    abort(409, message="A user with that username already exists.")

  user = User(
    username=user_data["username"],
    email=user_data["email"],
    password=pbkdf2_sha256.hash(user_data["password"])
  )
  db.session.add(user)
  db.session.commit()

  return user