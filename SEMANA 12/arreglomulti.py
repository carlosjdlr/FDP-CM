import random

# Definir las dimensiones: 3 ciudades, 7 días (de lunes a domingo), 4 semanas
ciudades = 3
dias = 7
semanas = 4

# Crear una matriz 3D para almacenar las temperaturas
temperaturas = [[[random.uniform(15, 35) for _ in range(dias)] for _ in range(semanas)] for _ in range(ciudades)]

# Lista de nombres de las ciudades (opcional)
nombres_ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C']

# Calcular el promedio de temperaturas para cada ciudad por semana
for ciudad_index in range(ciudades):
    print(f"\nPromedio de temperaturas para {nombres_ciudades[ciudad_index]}:")

    for semana_index in range(semanas):
        total_temperatura = 0

        for dia_index in range(dias):
            total_temperatura += temperaturas[ciudad_index][semana_index][dia_index]

        promedio_semana = total_temperatura / dias
        print(f"  Semana {semana_index + 1}: {promedio_semana:.2f}°C")
