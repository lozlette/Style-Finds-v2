from app import app
from flask import Blueprint, jsonify, request
from models.user import users_schema, user_schema, User

api = Blueprint('users', __name__)

@app.route("/users/", methods=['GET'])
def users():
    users = User.query.all()
    print(User.age)
    return users_schema.jsonify(users)

@app.route("/users/<id>", methods=['GET'])
def user_detail(id):
    user = User.get(id)
    return user_schema.jsonify(user)