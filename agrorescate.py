from animal import Animal
from recurso import Recurso
from lista_animales import ListaAnimales
from lista_recursos import ListaRecursos
from plan_alimentacion import PlanAlimentacion


class Agrorescate:
    def __init__(self):
        self.animales = ListaAnimales()
        self.recursos = ListaRecursos()
        self.plan = None

    def registrar_animal(self, tipo, cantidad, consumo_diario):
        self.animales.agregar(Animal(tipo, cantidad, consumo_diario))

    def registrar_recurso(self, tipo_alimento, cantidad_alimento, cantidad_agua):
        self.recursos.agregar(Recurso(tipo_alimento, cantidad_alimento, cantidad_agua))

    def generar_diagnostico(self, dias_sequia):
        consumo = self.animales.consumo_total()
        alimento = self.recursos.alimento_total()
        self.plan = PlanAlimentacion(dias_sequia)
        self.plan.calcular_necesidad(consumo, alimento)
        self.plan.generar_plan(self.animales.a_lista(), alimento)

    def mostrar_resultados(self):
        if self.plan is None:
            print("Primero genera el diagnóstico (opción 3).")
            return
        consumo = self.animales.consumo_total()
        alimento = self.recursos.alimento_total()
        dias_alcanza = alimento / consumo if consumo > 0 else 0

        print("\n--- DIAGNÓSTICO ---")
        print(f"Consumo diario total: {consumo} kg")
        print(f"Alimento disponible: {alimento} kg")
        print(f"Agua disponible: {self.recursos.agua_total()} L")
        print(f"El alimento alcanza para {dias_alcanza:.1f} días")
        print(f"Días de sequía: {self.plan.dias_sequia}")
        print(f"Alimento necesario: {self.plan.alimento_necesario} kg")
        print(f"Alimento faltante: {self.plan.alimento_faltante} kg")

        print("\n--- Plan por prioridad ---")
        for animal, necesita, asignado in self.plan.asignaciones:
            estado = "COMPLETO" if asignado >= necesita else "INSUFICIENTE"
            print(f"{animal} -> necesita {necesita} kg, recibe {asignado} kg [{estado}]")


def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Debe ser un número positivo")
                continue
            return valor
        except ValueError:
            print("Escribe un número válido")


def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Debe ser un número positiv")
                continue
            return valor
        except ValueError:
            print("Escribe un número entero válido")


def menu():
    app = Agrorescate()
    while True:
        print("\n--- AGRORESCATE ---")
        print("1. Registrar animal")
        print("2. Registrar recurso")
        print("3. Generar diagnóstico")
        print("4. Mostrar resultados")
        print("5. Ver animales y recursos registrados")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            tipo = input("Tipo de animal (vaca, caballo, cerdo, gallina): ")
            cantidad = pedir_entero("Cantidad: ")
            consumo = pedir_numero("Consumo diario por animal (kg): ")
            app.registrar_animal(tipo, cantidad, consumo)
            print("Animal registrado")
        elif opcion == "2":
            tipo = input("Tipo de alimento (heno, concentrado): ")
            alimento = pedir_numero("Cantidad de alimento (kg): ")
            agua = pedir_numero("Cantidad de agua (litros): ")
            app.registrar_recurso(tipo, alimento, agua)
            print("Recurso registrado")
        elif opcion == "3":
            if app.animales.contar() == 0 or app.recursos.alimento_total() == 0:
                print("Registra al menos un animal y un recurso primero")
            else:
                dias = pedir_entero("Días de sequía a cubrir: ")
                app.generar_diagnostico(dias)
                print("Diagnóstico generado, usa la opción 4 para verlo")
        elif opcion == "4":
            app.mostrar_resultados()
        elif opcion == "5":
            print("\nAnimales:")
            app.animales.mostrar()
            print("Recursos:")
            app.recursos.mostrar()
        elif opcion == "6":
            print("Hasta luego")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()