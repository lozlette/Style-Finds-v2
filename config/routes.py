from app import app
from flask import Blueprint, jsonify, request
from models.user import users_schema, user_schema, User

@app.route("/api/users/", methods=['GET'])
def users():
    all_users = dir(User)
    print(User.name)
    return users_schema.dump(all_users)

@app.route("/api/users/<id>", methods=['GET'])
def user_detail(id):
    user = User.get(id)
    return user_schema.dump(user)