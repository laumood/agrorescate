class Recurso:
    def __init__(self, tipo_alimento, cantidad_alimento, cantidad_agua):
        self.tipo_alimento = tipo_alimento
        self.cantidad_alimento = cantidad_alimento  
        self.cantidad_agua = cantidad_agua         

    def calcular_dias(self, consumo_diario):
        if consumo_diario <= 0:
            return 0
        return self.cantidad_alimento / consumo_diario

    def verificar_disponibilidad(self, consumo_diario, dias):
        return self.cantidad_alimento >= consumo_diario * dias

    def __str__(self):
        return f"{self.tipo_alimento}: {self.cantidad_alimento} kg de alimento, {self.cantidad_agua} L de agua"