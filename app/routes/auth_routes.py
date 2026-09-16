from flask import Blueprint

from app.controllers.auth_controller import register
from app.controllers.auth_controller import login
from app.controllers.auth_controller import protected


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/api/auth/register', methods=['POST'])
def register_route():
    return register()

@auth_bp.route('/api/auth/login', methods=['POST'])
def login_route():
    return login()

@auth_bp.route('/api/auth/protected', methods=['GET'])
def protected_route():
    return protected()