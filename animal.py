class Animal:
    def __init__(self, tipo, cantidad, consumo_diario):
        self.tipo = tipo
        self.cantidad = cantidad
        self.consumo_diario = consumo_diario
        self.nivel_prioridad = self.determinar_prioridad()

    def calcular_consumo(self):
        return self.cantidad * self.consumo_diario

    def determinar_prioridad(self):
        prioridades = {"vaca": 1, "caballo": 2, "cerdo": 2, "gallina": 3}
        return prioridades.get(self.tipo.lower(), 3)

    def __str__(self):
        return f"{self.tipo} x{self.cantidad} (prioridad {self.nivel_prioridad})"


if __name__ == "__main__":
    a = Animal("vaca", 10, 12)
    print(a)
    print("Consumo diario:", a.calcular_consumo(), "kg")