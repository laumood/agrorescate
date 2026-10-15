from nodo import Nodo
from recurso import Recurso


class ListaRecursos:
    def __init__(self):
        self.primero = None

    def agregar(self, recurso):
        nuevo = Nodo(recurso)
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
            print("No hay recursos registrados")
        while actual:
            print(" ", actual.dato)
            actual = actual.siguiente




    def alimento_total(self):
        return self._alimento_total(self.primero)

    def _alimento_total(self, nodo):
        if nodo is None:
            return 0
        return nodo.dato.cantidad_alimento + self._alimento_total(nodo.siguiente)

    def agua_total(self):
        return self._agua_total(self.primero)

    def _agua_total(self, nodo):
        if nodo is None:
            return 0
        return nodo.dato.cantidad_agua + self._agua_total(nodo.siguiente)


if __name__ == "__main__":
    lista = ListaRecursos()
    lista.agregar(Recurso("heno", 500, 200))
    lista.agregar(Recurso("concentrado", 300, 100))
    lista.mostrar()
    print("Alimento total:", lista.alimento_total())
    print("Agua total:", lista.agua_total())