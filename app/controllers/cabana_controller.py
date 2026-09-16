from flask import request

from app.middlewares.auth_middleware import validar_token, validar_rol
from app.services.cabana_service import registrar_cabana


def crear_cabana():

    payload, error = validar_token()

    if error:
        return {
            "error": error
        }, 401

    autorizado, error = validar_rol(
        payload,
        "administrador"
    )

    if not autorizado:
        return {
            "error": error
        }, 403

    datos = request.get_json()

    if not datos:
        return {
            "error": "Los datos de la cabaña son obligatorios"
        }, 400

    try:
        cabana = registrar_cabana(
            datos.get("nombre"),
            datos.get("descripcion"),
            datos.get("estado"),
            datos.get("direccion"),
            datos.get("max_capacidad"),
            datos.get("permite_ninos", True),
            payload["sub"]
        )

        return {
            "mensaje": "Cabaña creada correctamente",
            "cabana": {
                "id_cabana": cabana.id_cabana,
                "nombre": cabana.nombre,
                "descripcion": cabana.descripcion,
                "estado": cabana.estado,
                "direccion": cabana.direccion,
                "max_capacidad": cabana.max_capacidad,
                "permite_ninos": cabana.permite_ninos,
                "id_propietario": cabana.id_propietario
            }
        }, 201

    except ValueError as error:
        return {
            "error": str(error)
        }, 400