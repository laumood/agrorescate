from nodo import Nodo
from animal import Animal


class ListaAnimales:
    def __init__(self):
        self.primero = None

    def agregar(self, animal):
        nuevo = Nodo(animal)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.primero
        if actual is None:
            print("No hay animales registrados")
        while actual:
            print(" ", actual.dato)
            actual = actual.siguiente

    def a_lista(self):
        resultado = []
        actual = self.primero
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado




    def consumo_total(self):
        return self._consumo_total(self.primero)

    def _consumo_total(self, nodo):
        if nodo is None:         
            return 0
        return nodo.dato.calcular_consumo() + self._consumo_total(nodo.siguiente)

    def contar(self):
        return self._contar(self.primero)

    def _contar(self, nodo):
        if nodo is None:       
            return 0
        return 1 + self._contar(nodo.siguiente)


if __name__ == "__main__":
    lista = ListaAnimales()
    lista.agregar(Animal("vaca", 10, 12))
    lista.agregar(Animal("gallina", 30, 0.1))
    lista.mostrar()
    print("Consumo total:", lista.consumo_total())
    print("Cantidad de grupos:", lista.contar())