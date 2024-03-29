from alchemyClasses import db

class Peliculas(db.Model):
    __tablename__ = 'peliculas'
    idPelicula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    genero = db.Column(db.String(45))
    duracion = db.Column(db.Integer)
    inventario = db.Column(db.Integer, default=1)

    def __init__(self, nombre, genero=None, duracion=None, inventario=None):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f"Película: {self.nombre}, Género: {self.genero}, Duración: {self.duracion}"
