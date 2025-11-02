
from modelo_gallina import Gallina

class BaseDatos:
    def __init__(self):
        self.gallinas = []

    def crear_gallina(self, gallina):
        self.gallinas.append(gallina)

    def leer_gallinas(self):
        return self.gallinas

    def buscar_gallina(self, codigo):
        for g in self.gallinas:
            if g.codigo == codigo:
                return g
        return None

    def eliminar_gallina(self, codigo):
        for i, g in enumerate(self.gallinas):
            if g.codigo == codigo:
                self.gallinas.pop(i)
                return True
        return False
    
    def actualizar_codigo(self, codigo_actual, nuevo_codigo):
        for g in self.gallinas:
            if g.codigo == codigo_actual:
                g.codigo = nuevo_codigo
                return True
        return False
