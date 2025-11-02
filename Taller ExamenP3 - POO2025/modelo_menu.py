
import random
from modelo_gallina import Gallina
from modelo_base_de_datos import BaseDatos

class Menu:
    def __init__(self):
        self.bd = BaseDatos()

    def iniciar(self):
        while True:
            print("\n#### MENÚ PRINCIPAL ####")
            print("1. Registrar nueva gallina")
            print("2. Ver lista de gallinas")
            print("3. Revisar huevos semanales de una gallina")
            print("4. Actualizar código de gallina")
            print("5. Consultar producción total de una gallina")
            print("6. Eliminar una gallina")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    self.registrar_gallina()
                case "2":
                    self.ver_gallinas()
                case "3":
                    self.revizar_huevos()
                case "4":
                    self.actualizar_gallina()
                case "5":
                    self.ver_produccion_total()
                case "6":
                    self.eliminar_gallina()
                case "7":
                    print("Programa finalizado.")
                    break
                case _:
                    print("Opción inválida, intente de nuevo.")

    def registrar_gallina(self):
        codigo = input("Código de la gallina: ")
        if self.bd.buscar_gallina(codigo):
            print(" Ese código ya existe.")
            return
        gallina = Gallina(codigo)
        self.bd.crear_gallina(gallina)
        print(" La gallina se ha registrado correctamente.")

    def ver_gallinas(self):
        gallinas = self.bd.leer_gallinas()
        if not gallinas:
            print("No hay gallinas registradas.")
        else:
            for g in gallinas:
                print(f"Código: {g.codigo}, Semanas registradas: {len(g.produccion)}")

    def revizar_huevos(self):
        codigo = input("Código de la gallina: ")
        gallina = self.bd.buscar_gallina(codigo)
        if gallina:
            huevos = random.randint(2, 6)
            gallina.agregar_huevos(huevos)
            print(f" Se encontraron {huevos} huevos esta semana.")
        else:
            print("No se encontro una gallina con ese código o no existe.")

    def actualizar_gallina(self):
        codigo_actual = input("Código actual de la gallina: ")
        gallina = self.bd.buscar_gallina(codigo_actual)

        if not gallina:
            print("No se encontro una gallina con ese código o no existe.")
            return
        
        nuevo_codigo = input("Nuevo código de la gallina: ")

        if self.bd.buscar_gallina(nuevo_codigo):
            print("Ya existe una gallina con ese código.")
            return

        self.bd.actualizar_codigo(codigo_actual, nuevo_codigo)
        print("Código actualizado correctamente.")
        
    def ver_produccion_total(self):
        codigo = input("Código de la gallina: ")
        gallina = self.bd.buscar_gallina(codigo)
        if gallina:
            semanas = len(gallina.produccion)
            print(f"Producción total de la gallina {codigo} fue de {gallina.produccion_total()} huevos en {len(gallina.produccion)} semanas.")
        else:
            print("No se encontro una gallina con ese código o no existe.")

    def eliminar_gallina(self):
        codigo = input("Código de la gallina a eliminar: ")
        eliminar = self.bd.eliminar_gallina(codigo)
        if eliminar:
            print("Registro eliminado.")
        else:

            print("No se encontro una gallina con ese código o no existe.")
