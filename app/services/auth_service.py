from werkzeug.security import generate_password_hash

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