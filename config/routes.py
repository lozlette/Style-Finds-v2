from app import app
from controllers import users, styles

app.register_blueprint(users.api, url_prefix='/api')
app.register_blueprint(styles.api, url_prefix='/api')

