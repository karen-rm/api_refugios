from flask import Blueprint

from app.controllers.cabana_controller import crear_cabana
from app.middlewares.auth_middleware import validar_token, validar_rol


cabana_bp = Blueprint('cabana', __name__)


@cabana_bp.route('/api/cabana/admin-prueba', methods=['GET'])
def prueba_admin():

    payload, error = validar_token()

    if error:
        return {"error": error}, 401

    autorizado, error = validar_rol(
        payload,
        "administrador"
    )

    if not autorizado:
        return {"error": error}, 403

    return {
        "mensaje": "Acceso autorizado",
        "usuario_id": payload["sub"],
        "rol": payload["rol"]
    }, 200


@cabana_bp.route('/api/cabana', methods=['POST'])
def crear_cabana_route():
    return crear_cabana()