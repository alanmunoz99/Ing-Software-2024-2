from alchemyClasses import db
from datetime import datetime

class Rentar(db.Model):
    __tablename__ = 'rentar'
    idRentar = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuarios.idUsuario'), nullable=False)
    idPelicula = db.Column(db.Integer, db.ForeignKey('peliculas.idPelicula'), nullable=False)
    fecha_renta = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dias_de_renta = db.Column(db.Integer, default=5)
    estatus = db.Column(db.Boolean, default=False)

    def __init__(self, idUsuario, idPelicula, fecha_renta=None, dias_de_renta=None, estatus=None):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        return f"Rentar: Usuario {self.idUsuario}, Película {self.idPelicula}, Fecha {self.fecha_renta}"