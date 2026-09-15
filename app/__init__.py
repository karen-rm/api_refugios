from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from app.models.models import db
from app.middlewares.error_handler import register_error_handlers



load_dotenv()


def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    register_error_handlers(app)

    from app.routes.health_routes import health_bp
    app.register_blueprint(health_bp)

    return app