class Producto:
    # constructor de la clase Producto
    def __init__(self, nombre, precio,  id_producto=0):
        self._idproducto = id_producto
        self._nombre = nombre
        self._precio = precio

    # getters de la clase producto
    @property
    def idproducto(self):
        return self._idproducto

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    # TODO: faltan los setters y el metodo toString