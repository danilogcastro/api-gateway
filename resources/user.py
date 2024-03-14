from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256

from db import db
from models import User
from schemas import UserSchema
from schemas import UserLoginSchema

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

@blp.post("/users/login")
@blp.arguments(UserLoginSchema)
def login(user_data):
  user = User.query.filter(User.email == user_data["email"]).first()

  if user and pbkdf2_sha256.verify(user_data["password"], user.password):
    access_token = create_access_token(identity=user.id)
    return { "access_token": access_token }, 200

  abort(401, message="Invalid credentials.")
