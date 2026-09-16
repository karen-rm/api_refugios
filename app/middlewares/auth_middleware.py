import os

import jwt
from flask import request


def validar_token():

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return None, "Se requiere un token"

    try:
        esquema, token = auth_header.split(" ", 1)

        if esquema.lower() != "bearer":
            return None, "Formato de token inválido"

        payload = jwt.decode(
            token,
            os.getenv("JWT_SECRET_KEY"),
            algorithms=["HS256"]
        )

        return payload, None

    except jwt.ExpiredSignatureError:
        return None, "El token ha expirado"

    except jwt.InvalidTokenError:
        return None, "Token inválido"

    except ValueError:
        return None, "Formato de autorización inválido"