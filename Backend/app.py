from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db
from config import Config
from routes.auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)
CORS(app)

app.register_blueprint(auth_bp, url_prefix="/api/auth")

if __name__ == "__main__":
    app.run(debug=True)
