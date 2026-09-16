from werkzeug.security import generate_password_hash, check_password_hash
from app.services.jwt_service import crear_token

from app.repositories.usuario_repository import (
    buscar_por_correo,
    crear_usuario
)

def registrar_usuario(correo, contrasena):

    usuario_existente = buscar_por_correo(correo)

    if usuario_existente:
        return None, "El correo ya está registrado"

    contrasena_hash = generate_password_hash(contrasena)

    usuario = crear_usuario(
        correo,
        contrasena_hash
    )

    return usuario, None


def verificar_password(contrasena, contrasena_hash):
    return check_password_hash(contrasena_hash, contrasena)


def iniciar_sesion(correo, contrasena):

    usuario = buscar_por_correo(correo)

    if not usuario:
        raise ValueError("Credenciales inválidas")

    if not verificar_password(
        contrasena,
        usuario.contrasena
    ):
        raise ValueError("Credenciales inválidas")

    token = crear_token(
        usuario.id_usuario,
        usuario.rol
    )

    return {
        "token": token,
        "usuario": {
            "id_usuario": usuario.id_usuario,
            "correo": usuario.correo,
            "rol": usuario.rol
        }
    }