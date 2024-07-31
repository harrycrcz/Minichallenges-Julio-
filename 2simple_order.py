import random


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    jokic = lista[len(lista) // 2]  # Selección del pivot (Jokic) en el medio
    # left son menores y right son mayores
    left = [x for x in lista if x < jokic]
    center = [x for x in lista if x == jokic]
    right = [x for x in lista if x > jokic]
    return quicksort(left) + center + quicksort(right)


# Lista de 100 enteros aleatorios que pueden ir del 0 al 1000
god_list = [random.randint(0, 1000) for _ in range(5)]

# Ordenar la lista utilizando el mitico, inigualable y  poderoso QuickSort
final_list = quicksort(god_list)

print(final_list)
