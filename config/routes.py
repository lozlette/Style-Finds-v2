from models import user, users_schema, user_schema
from app import app

from app import app
from models import User

@app.route("api/users/")
def users():
    all_users = User.all
    return users_schema.dump(all_users)

@app.route("api/users/<id>")
def user_detail(id):
    user = User.get(id)
    return user_schema.dump(user)