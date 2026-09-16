from app.repositories.cabana_repository import crear_cabana, obtener_cabanas


def registrar_cabana(
    nombre,
    descripcion,
    estado,
    direccion,
    max_capacidad,
    permite_ninos,
    id_propietario
):
    if not nombre:
        raise ValueError("El nombre de la cabaña es obligatorio")

    if not max_capacidad or max_capacidad <= 0:
        raise ValueError("La capacidad máxima debe ser mayor a 0")

    return crear_cabana(
        nombre,
        descripcion,
        estado,
        direccion,
        max_capacidad,
        permite_ninos,
        id_propietario
    )

def listar_cabanas():
    return obtener_cabanas()