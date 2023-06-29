import sys
import psycopg2 as bd


class Conexion:
    _DATABASE = 'Cafeteria'
    _USERNAME = 'postgres'
    _PASSWORD = 'Balles1653'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    @classmethod
    def crearBaseDeDatos(cls):
        try:
            conexion = bd.connect(host=cls._HOST,
                                  user=cls._USERNAME,
                                  password=cls._PASSWORD,
                                  port=cls._DB_PORT)
            cursor = conexion.cursor()

            # Verificar si la base de datos ya existe
            cursor.execute(
                "SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s;", (cls._DATABASE,))
            existe = cursor.fetchone()

            if existe:
                print(f"La base de datos '{cls._DATABASE}' ya existe.")
            else:
                cursor.execute(f"CREATE DATABASE {cls._DATABASE}")
                conexion.commit()
                print(
                    f"La base de datos '{cls._DATABASE}' ha sido creada exitosamente.")

            cursor.close()
            conexion.close()
        except Exception as e:
            print(
                f"Ocurrió un error al crear o verificar la base de datos: {e}")
            sys.exit()

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                return cls._conexion
            except Exception as e:
                print(f'Ocurrió un error: {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                return cls._cursor
            except Exception as e:
                print(f'Ocurrió un ERROR: {e}')
                sys.exit()
        else:
            return cls._cursor

    @classmethod
    def ejecutarConsulta(cls, consulta):
        try:
            cursor = cls.obtenerCursor()
            cursor.execute(consulta)
            datos = cursor.fetchall()
            return datos
        except Exception as e:
            print(f'Ocurrió un error al ejecutar la consulta: {e}')
            sys.exit()
