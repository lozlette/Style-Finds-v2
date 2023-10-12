from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config.environment import db_uri


app = Flask(__name__)

app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = db_uri

db = SQLAlchemy(app)

ma = Marshmallow(app)

@app.route('/')
def helloworld():
    return "Hello World"

# if __name__ == '__main__':
#     app.run()

from config import routes