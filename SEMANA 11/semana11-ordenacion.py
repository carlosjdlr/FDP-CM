def ordenar_fila(matriz, fila_index):
    fila = matriz[fila_index]
    fila.sort()
    return matriz


if __name__ == "__main__":
    matriz = [
        [9, 7, 5],
        [8, 6, 4],
        [3, 1, 2]
    ]

    print("Matriz Original:")
    for fila in matriz:
        print(fila)

    fila_index = int(input("Introduce el índice de la fila a ordenar (0-2): "))
    if 0 <= fila_index < len(matriz):
        matriz_ordenada = ordenar_fila(matriz, fila_index)
        print("Matriz con la fila ordenada:")
        for fila in matriz_ordenada:
            print(fila)
    else:
        print("Índice de fila no válido.")