from flask import Blueprint

from app.controllers.auth_controller import register


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/api/auth/register', methods=['POST'])
def register_route():
    return register()
