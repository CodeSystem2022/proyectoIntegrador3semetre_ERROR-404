import sys
import psycopg2 as bd


class Conexion:
    _DATABASE = 'Cafeteria'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

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

        try:
            cls._cursor = cls.obtenerConexion().cursor()
            return cls._cursor
        except Exception as e:
            print(f'Ocurrió un ERROR: {e}')
