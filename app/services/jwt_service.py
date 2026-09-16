import os
import jwt
from datetime import datetime, timedelta, timezone


def crear_token(usuario_id, rol):
    ahora = datetime.now(timezone.utc)

    expiracion = int(os.getenv("JWT_EXPIRATION_HOURS", "2"))

    payload = {
        "sub": str(usuario_id),
        "rol": rol,
        "iat": ahora,
        "exp": ahora + timedelta(hours=expiracion)
    }

    return jwt.encode(
        payload,
        os.getenv("JWT_SECRET_KEY"),
        algorithm="HS256"
    )