from alchemyClasses import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    apPat = db.Column(db.String(200), nullable=False)
    apMat = db.Column(db.String(200))
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(500), unique=True)
    profilePicture = db.Column(db.LargeBinary)
    superUser = db.Column(db.Boolean)

    def __init__(self, nombre, apPat, apMat=None, password=None, email=None, profilePicture=None, superUser=None):
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apPat} {self.apMat}, Email: {self.email}"