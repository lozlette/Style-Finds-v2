from app import app
from flask import Blueprint, jsonify, request
from models.find import finds_schema, find_schema, Find

api = Blueprint('finds', __name__)

@app.route("/finds/", methods=['GET'])
def finds():
    finds = Find.query.all()
    return finds_schema.jsonify(finds)

@app.route("/finds/<id>", methods=['GET'])
def find_detail(id):
    find = Find.get(id)
    return find_schema.jsonify(Find)