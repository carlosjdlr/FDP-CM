def buscar_en_matriz(matriz, valor):
    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            if elemento == valor:
                return (i, j)
    return None


if __name__ == "__main__":
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    valor_buscar = int(input("Introduce el valor a buscar en la matriz: "))
    resultado = buscar_en_matriz(matriz, valor_buscar)

    if resultado:
        print(f"Valor {valor_buscar} encontrado en la posición {resultado}.")
    else:
        print(f"Valor {valor_buscar} no encontrado en la matriz.")