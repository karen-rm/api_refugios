from flask import jsonify, request

from app.services.auth_service import registrar_usuario
from app.services.auth_service import iniciar_sesion
from app.middlewares.auth_middleware import validar_token



def register():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Bad Request",
            "mensaje": "Se requiere un cuerpo JSON"
        }), 400

    correo = data.get('correo')
    contrasena = data.get('contrasena')

    if not correo or not contrasena:
        return jsonify({
            "error": "Bad Request",
            "mensaje": "El correo y la contraseña son obligatorios"
        }), 400

    usuario, error = registrar_usuario(
        correo,
        contrasena
    )

    if error:
        return jsonify({
            "error": "Conflict",
            "mensaje": error
        }), 409

    return jsonify({
        "mensaje": "Usuario registrado correctamente",
        "usuario": {
            "id_usuario": usuario.id_usuario,
            "correo": usuario.correo,
            "rol": usuario.rol
        }
    }), 201

def login():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Bad Request",
            "mensaje": "Se requiere un cuerpo JSON"
        }), 400

    correo = data.get("correo")
    contrasena = data.get("contrasena")

    if not correo or not contrasena:
        return jsonify({
            "error": "Bad Request",
            "mensaje": "El correo y la contraseña son obligatorios"
        }), 400

    resultado = iniciar_sesion(
        correo,
        contrasena
    )

    return jsonify(resultado), 200

def me():

    payload, error = validar_token()

    if error:
        return jsonify({
            "error": "Unauthorized",
            "mensaje": error
        }), 401

    usuario_id = payload["sub"]

    # aquí posteriormente buscamos al usuario

def protected():
    payload, error = validar_token()

    if error:
        return jsonify({
            "error": error
        }), 401

    return jsonify({
        "mensaje": "Acceso autorizado",
        "usuario": payload
    }), 200