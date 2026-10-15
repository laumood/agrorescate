from cola import Cola


class PlanAlimentacion:
    def __init__(self, dias_sequia):
        self.dias_sequia = dias_sequia
        self.alimento_necesario = 0
        self.alimento_faltante = 0
        self.asignaciones = []  

    def calcular_necesidad(self, consumo_total, alimento_disponible):
        self.alimento_necesario = consumo_total * self.dias_sequia
        self.alimento_faltante = max(0, self.alimento_necesario - alimento_disponible)

    def generar_plan(self, animales, alimento_disponible):
        ordenados = sorted(animales, key=lambda a: a.nivel_prioridad)

        cola = Cola()
        for animal in ordenados:
            cola.encolar(animal)

        restante = alimento_disponible
        self.asignaciones = []
        while not cola.esta_vacia():
            animal = cola.desencolar()
            necesita = animal.calcular_consumo() * self.dias_sequia
            asignado = min(necesita, restante)
            restante -= asignado
            self.asignaciones.append((animal, necesita, asignado))