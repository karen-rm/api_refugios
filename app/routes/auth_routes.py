from flask import Blueprint

from app.controllers.auth_controller import register
from app.controllers.auth_controller import login


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/api/auth/register', methods=['POST'])
def register_route():
    return register()

@auth_bp.route('/api/auth/login', methods=['POST'])
def login_route():
    return login()