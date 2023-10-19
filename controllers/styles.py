from app import app
from flask import Blueprint, jsonify, request
from models.style import styles_schema, style_schema, Style

api = Blueprint('styles', __name__)

@app.route("/styles/", methods=['GET'])
def styles():
    styles = Style.query.all()
    return styles_schema.jsonify(styles)

@app.route("/styles/<id>", methods=['GET'])
def style_detail(id):
    style = Style.get(id)
    return style_schema.jsonify(style)