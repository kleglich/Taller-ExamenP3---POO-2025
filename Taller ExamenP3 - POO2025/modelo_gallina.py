
class Gallina : 
    def __init__(self, codigo):
        self.codigo = codigo
        self.produccion = []
        
    def agregar_huevos(self, cantidad):
        self.produccion.append(cantidad)

    def produccion_total(self):
        return sum(self.produccion)

    def imprimir_produccion(self):
        for p in self.produccion:
            print(p)

