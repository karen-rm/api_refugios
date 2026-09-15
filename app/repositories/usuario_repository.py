from app.models.models import Usuario, db


def buscar_por_correo(correo):
    return Usuario.query.filter_by(correo=correo).first()


def crear_usuario(correo, contrasena):
    usuario = Usuario(
        correo=correo,
        contrasena=contrasena,
        rol='usuario'
    )

    db.session.add(usuario)
    db.session.commit()

    return usuario