from app.models.models import Cabana, db


def crear_cabana(
    nombre,
    descripcion,
    estado,
    direccion,
    max_capacidad,
    permite_ninos,
    url_imagen,
    id_propietario
):
    cabana = Cabana(
        nombre=nombre,
        descripcion=descripcion,
        estado=estado,
        direccion=direccion,
        max_capacidad=max_capacidad,
        permite_ninos=permite_ninos,
        url_imagen=url_imagen,
        id_propietario=id_propietario
    )

    db.session.add(cabana)
    db.session.commit()

    return cabana


def obtener_cabanas():
    return Cabana.query.all()