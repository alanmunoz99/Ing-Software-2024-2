import pymysql
import datetime

def insertar_registros():
    # Conexión a la base de datos
    conexion = pymysql.connect(host='localhost',
                               user='lab',
                               password='Developer123!',
                               database='lab_ing_software')

    try:
        with conexion.cursor() as cursor:
            # Insertar en la tabla usuarios
            sql = "INSERT INTO usuarios (nombre, apPat, apMat, password, email) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, ('Alan', 'Muñoz', 'Sandoval', 'contraseña', 'alanmunoz@ciencias.unam.mx'))
            # Obtener el ID generado para la nueva fila
            id_usuario = cursor.lastrowid

            # Insertar en la tabla peliculas
            sql = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, ('Taxi Driver', 'Thriller Psicologico', 114, 10))
            # Obtener el ID generado para la nueva fila
            id_pelicula = cursor.lastrowid

            # Insertar en la tabla rentar
            sql = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (id_usuario, id_pelicula, '2024-03-27 12:00:00', 5, 1))

        # Confirmar la transacción
        conexion.commit()
        print("Registros insertados correctamente.")

    except Exception as e:
        # En caso de error, deshacer la transacción
        print("Error:", e)
        conexion.rollback()

    finally:
        # Cerrar la conexión
        conexion.close()

# Llamar a la función para insertar registros
insertar_registros()


def filtrar_usuarios_por_apellido(apellido):
    # Conexión a la base de datos
    conexion = pymysql.connect(host='localhost',
                               user='lab',
                               password='Developer123!',
                               database='lab_ing_software')

    try:
        with conexion.cursor() as cursor:
            # Filtrar usuarios por apellido
            sql = "SELECT * FROM usuarios WHERE apMat LIKE %s OR apPat LIKE %s"
            cursor.execute(sql, (f'%{apellido}', f'%{apellido}'))
            usuarios = cursor.fetchall()
            # Mostrar resultados
            for usuario in usuarios:
                print(usuario)

    except Exception as e:
        print("Error:", e)

    finally:
        conexion.close()

# Llamar a la función para filtrar usuarios por apellido
filtrar_usuarios_por_apellido('Muñoz')


def cambiar_genero_pelicula(nombre_pelicula, nuevo_genero):
    # Conexión a la base de datos
    conexion = pymysql.connect(host='localhost',
                               user='lab',
                               password='Developer123!',
                               database='lab_ing_software')

    try:
        with conexion.cursor() as cursor:
            # Verificar si la película existe
            sql = "SELECT * FROM peliculas WHERE nombre = %s"
            cursor.execute(sql, (nombre_pelicula,))
            pelicula = cursor.fetchone()
            if pelicula:
                # Cambiar el género de la película
                sql = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
                cursor.execute(sql, (nuevo_genero, nombre_pelicula))
                conexion.commit()
                print("Género de la película actualizado correctamente.")
            else:
                print("La película especificada no existe.")

    except Exception as e:
        print("Error:", e)

    finally:
        conexion.close()

# Llamar a la función para cambiar el género de una película
cambiar_genero_pelicula('Taxi Driver', 'Thriller Psicologico Neo Noir')


def eliminar_rentas_antiguas():
    # Conexión a la base de datos
    conexion = pymysql.connect(host='localhost',
                               user='lab',
                               password='Developer123!',
                               database='lab_ing_software')

    try:
        with conexion.cursor() as cursor:
            # Calcular fecha límite (3 días atrás)
            fecha_limite = datetime.datetime.now() - datetime.timedelta(days=3)
            # Eliminar rentas antiguas
            sql = "DELETE FROM rentar WHERE fecha_renta <= %s"
            cursor.execute(sql, (fecha_limite,))
            conexion.commit()
            print("Rentas antiguas eliminadas correctamente.")

    except Exception as e:
        print("Error:", e)

    finally:
        conexion.close()

# Llamar a la función para eliminar rentas antiguas
eliminar_rentas_antiguas()