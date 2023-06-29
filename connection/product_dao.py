import sys
from connection import Conexion
from connection.product import Producto


class ProductDAO:
    #Creación de consultas y asignación a variables
    _SELECCIONAR = 'SELECT * FROM producto ORDER BY id_producto'
    _INSERTAR = 'INSERT INTO producto(nombre, precio) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE producto SET nombre=%s, precio=%s WHERE id_producto=%s'
    _ELIMINAR = 'DELETE FROM producto WHERE id_producto=%s'

    #Definimos los métodos de clases requeridos
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                productos = []
                try:
                    cursor.execute(cls._SELECCIONAR)
                    registros = cursor.fetchall()

                    for registro in registros:
                        producto1 = Producto(registro[0], registro[1], registro[2])
                        productos.append(producto1)
                except Exception as e:
                    print(f"Ocurrio un Error: {e}")

                return productos

    @classmethod
    def insertar(cls, producto):
        with Conexion.obtenerConexion() as conn:
            with Conexion.obtenerCursor() as cursor:
                valores = (producto.nombre, producto.precio)
                try:

                    cursor.execute(cls._INSERTAR, valores)
                    conn.commit()

                except Exception as e:
                    print(f"Ocurrio un ERROR: ${e}")
                    sys.exit()
            return cursor.rowcount


"""
    @classmethod
    def actualizar(cls, producto):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (producto.nombre, producto.precio,
                           producto.id_producto)
                cursor.execute(cls._ACTUALIZAR, valores)
                return cursor.rowcount

    @classmethod
    def eliminar(cls, producto):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (producto.id_producto,)
                cursor.execute(cls._ELIMINAR, valores)
                return cursor.rowcount
"""