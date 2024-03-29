from alchemyClasses import db
from alchemyClasses.Usuarios import Usuarios
from alchemyClasses.Peliculas import Peliculas
from alchemyClasses.Rentar import Rentar

from hashlib import sha256
from datetime import datetime
from flask import Flask
from sqlalchemy import and_, or_

from alchemyClasses import db
from alchemyClasses.Alumno import Alumno
from cryptoUtils.CryptoUtils import cipher
from hashlib import sha256

from model.model_alumno import borra_alumno

#mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft
#<dialecto>+<driver>://<usuario>:<passwd>@localhost:3306/<db>
#mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_soft
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

def mostrar_registros(tabla):
    registros = tabla.query.all()
    for registro in registros:
        print(registro)

def filtrar_por_id(tabla, id):
    registro = tabla.query.filter_by(id=id).first()
    if registro:
        print(registro)
    else:
        print("No se encontró ningún registro con ese ID.")

def actualizar_nombre_renta(id_renta, nuevo_nombre):
    renta = Rentar.query.get(id_renta)
    if renta:
        renta.fecha_renta = datetime.utcnow()  # Modificar la fecha de la renta
        db.session.commit()
        print("Se actualizó la fecha de renta exitosamente.")
    else:
        print("No se encontró ninguna renta con el ID.")

def eliminar_registro(tabla, id=None):
    if id:
        registro = tabla.query.get(id)
        if registro:
            db.session.delete(registro)
            db.session.commit()
            print("Registro eliminado exitosamente.")
        else:
            print("No se encontró ningún registro con ese ID.")
    else:
        confirmacion = input("¿Está seguro que desea eliminar todos los registros de esta tabla? (s/n): ")
        if confirmacion.lower() == 's':
            tabla.query.delete()
            db.session.commit()
            print("Todos los registros han sido eliminados.")
        else:
            print("Operación cancelada.")

if __name__ == '__main__':
    with app.app_context():
        print("Menú:")
        print("1. Ver registros de una tabla.")
        print("2. Filtrar registros de una tabla por ID.")
        print("3. Actualizar la fecha de una renta.")
        print("4. Eliminar un registro por ID o todos los registros de una tabla.")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("Tablas disponibles:")
            print("1. Usuarios")
            print("2. Películas")
            print("3. Rentas")
            tabla_seleccionada = input("Seleccione una tabla: ")
            if tabla_seleccionada == '1':
                mostrar_registros(Usuarios)
            elif tabla_seleccionada == '2':
                mostrar_registros(Peliculas)
            elif tabla_seleccionada == '3':
                mostrar_registros(Rentar)
            else:
                print("Opción no válida.")

        elif opcion == '2':
            print("Tablas disponibles:")
            print("1. Usuarios")
            print("2. Películas")
            print("3. Rentas")
            tabla_seleccionada = input("Seleccione una tabla: ")
            id = input("Ingrese el ID a filtrar: ")
            if tabla_seleccionada == '1':
                filtrar_por_id(Usuarios, id)
            elif tabla_seleccionada == '2':
                filtrar_por_id(Peliculas, id)
            elif tabla_seleccionada == '3':
                filtrar_por_id(Rentar, id)
            else:
                print("Opción no válida.")

        elif opcion == '3':
            id_renta = input("Ingrese el ID de la renta a actualizar: ")
            nuevo_nombre = input("Ingrese la nueva fecha de renta (YYYY-MM-DD HH:MM:SS): ")
            actualizar_nombre_renta(id_renta, nuevo_nombre)

        elif opcion == '4':
            print("Tablas disponibles:")
            print("1. Usuarios")
            print("2. Películas")
            print("3. Rentas")
            tabla_seleccionada = input("Seleccione una tabla: ")
            id = input("Ingrese el ID del registro a eliminar (deje vacío para eliminar todos los registros): ")
            if tabla_seleccionada == '1':
                if id:
                    usuario = Usuarios.query.get(id)
                    if usuario:
                        Rentar.query.filter_by(idUsuario=id).delete()  # Eliminar rentas asociadas al usuario
                        db.session.delete(usuario)  # Eliminar el usuario
                        db.session.commit()
                        print("Usuario eliminado exitosamente.")
                    else:
                        print("No se encontró ningún usuario con ese ID.")
                else:
                    confirmacion = input("¿Está seguro que desea eliminar todos los usuarios? (s/n): ")
                    if confirmacion.lower() == 's':
                        Rentar.query.delete()  # Eliminar todas las rentas
                        Usuarios.query.delete()  # Eliminar todos los usuarios
                        db.session.commit()
                        print("Todos los usuarios y rentas han sido eliminados.")
                    else:
                        print("Operación cancelada.")
            elif tabla_seleccionada == '2':
                eliminar_registro(Peliculas, id)
            elif tabla_seleccionada == '3':
                eliminar_registro(Rentar, id)
            else:
                print("Opción no válida.")

    print("Operación completada.")




'''
if __name__ == '__main__':
    with app.app_context():
        print("Antes de Hacer")
        for alumno in Alumno.query.all():  # Select * from alumno
            print("Haciendo")
            print(alumno)

        """for alumno in Alumno.query.filter(and_(Alumno.nombre == 'Fer', Alumno.num_cta == 313320679)): #Un booleano a evaluar.
            print(f"Nombre de alumno con cta 313320679 es: {alumno.nombre}")"""

        # Create
        valeria = Alumno('Valeria', 'Ramirez', 319311918, apMat=None,
                         password=sha256(cipher("Developer123#")).hexdigest())
        db.session.add(valeria)
        db.session.commit()
        # Update
        # Primero tenemos que buscar el objeto que queremos.
        # Ya que lo tengo, entonces cambio el atributo.
        # Y entonces hago el commit.
        # fer = Alumno.query.filter(Alumno.nombre == 'Fernando').first()
        # print(type(fer))
        # fer.nombre = "Fer"
        # fer.ap_mat = "Baeza"
        # db.session.commit()
        # Delete
        """borra_alumno(313320679)"""
    print("Borrado con éxito!")
'''