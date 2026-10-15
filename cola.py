from collections import deque


class Cola:
    def __init__(self):
        self.items = deque()

    def encolar(self, dato):
        self.items.append(dato)

    def desencolar(self):
        return self.items.popleft()

    def esta_vacia(self):
        return len(self.items) == 0