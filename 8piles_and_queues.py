class Pila:
    def __init__(self, lista_vacia):
        self.lista_vacia = lista_vacia

    # sacar el ultimo elemento
    def pop_list(self):
        return self.lista_vacia.pop()

    # meter un elemento x
    def append_list(self, x):
        return self.lista_vacia.append(x)

    # verificar si esta vacia

    def is_empty(self):
        # aca me va a tirar True si esta vacia, y False si no.
        return self.lista_vacia == 0

    # ordenar la lista

    def sort(self):
        return self.lista_vacia.sort()
