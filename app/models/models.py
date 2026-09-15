from flask_sqlalchemy import SQLAlchemy

# Inicializamos la base de datos vacía
db = SQLAlchemy()

# --- TABLAS INTERMEDIAS ---
cabana_amenidad = db.Table('cabana_amenidad',
    db.Column('id_cabana_amenidad', db.Integer, primary_key=True, autoincrement=True),
    db.Column('id_cabana', db.Integer, db.ForeignKey('cabanas.id_cabana', ondelete='CASCADE'), nullable=False),
    db.Column('id_amenidad', db.Integer, db.ForeignKey('amenidades.id_amenidad', ondelete='CASCADE'), nullable=False)
)

cabana_zona = db.Table('cabana_zona',
    db.Column('id_cabana_zona', db.Integer, primary_key=True, autoincrement=True),
    db.Column('id_cabana', db.Integer, db.ForeignKey('cabanas.id_cabana', ondelete='CASCADE'), nullable=False),
    db.Column('id_zona', db.Integer, db.ForeignKey('zonas.id_zona', ondelete='CASCADE'), nullable=False)
)

# --- MODELOS PRINCIPALES ---
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rol = db.Column(db.String(20), nullable=False, default='usuario') 
    correo = db.Column(db.String(150), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)

class Zona(db.Model):
    __tablename__ = 'zonas'
    id_zona = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)

class Amenidad(db.Model):
    __tablename__ = 'amenidades'
    id_amenidad = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)

class Cabana(db.Model):
    __tablename__ = 'cabanas'
    id_cabana = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text)
    estado = db.Column(db.String(100))
    direccion = db.Column(db.String(255))
    max_capacidad = db.Column(db.Integer, nullable=False)
    permite_ninos = db.Column(db.Boolean, default=True)
    
    id_propietario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario', ondelete='CASCADE'), nullable=False)

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id_reserva = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_llegada = db.Column(db.DateTime, nullable=False)
    fecha_salida = db.Column(db.DateTime, nullable=False)
    adultos = db.Column(db.Integer, nullable=False)
    ninos = db.Column(db.Integer, default=0)
    
    id_cabana = db.Column(db.Integer, db.ForeignKey('cabanas.id_cabana', ondelete='CASCADE'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario', ondelete='CASCADE'), nullable=False)