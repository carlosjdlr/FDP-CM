# Función para calcular el promedio de temperaturas de varias ciudades
def calcular_promedio_temperaturas(temperaturas, ciudades):
    """
    Calcula el promedio de temperaturas para cada ciudad y muestra las temperaturas semanales.

    :param temperaturas: Lista de listas de temperaturas, donde cada sublista
                         contiene las temperaturas de una ciudad por semanas.
    :param ciudades: Lista con los nombres de las ciudades correspondientes a las temperaturas.
    :return: Lista de promedios por ciudad.
    """
    promedios = []

    # Recorrer cada ciudad y sus temperaturas
    for i, ciudad_temperaturas in enumerate(temperaturas):
        print(f"Temperaturas de {ciudades[i]} por semanas:")
        for semana, temperatura in enumerate(ciudad_temperaturas, 1):
            print(f"  Semana {semana}: {temperatura}°C")

        # Calcular el promedio para cada ciudad
        promedio_ciudad = sum(ciudad_temperaturas) / len(ciudad_temperaturas)
        promedios.append(promedio_ciudad)
        print(f"Promedio de temperatura en {ciudades[i]}: {promedio_ciudad:.2f}°C\n")

    return promedios


# Función para permitir al usuario ingresar una nueva ciudad y sus temperaturas
def agregar_nueva_ciudad(temperaturas, ciudades):
    """
    Permite agregar una nueva ciudad y sus temperaturas ingresadas por el usuario.

    :param temperaturas: Lista de listas de temperaturas existentes.
    :param ciudades: Lista con los nombres de las ciudades existentes.
    """
    # Solicitar el nombre de la nueva ciudad
    nueva_ciudad = input("Ingrese el nombre de la nueva ciudad: ")
    ciudades.append(nueva_ciudad)

    # Solicitar las temperaturas para la nueva ciudad (4 semanas)
    temperaturas_nuevas = []
    print(f"Ingrese las temperaturas para {nueva_ciudad} (durante 4 semanas):")
    for semana in range(1, 5):
        temperatura = float(input(f"  Semana {semana}: "))
        temperaturas_nuevas.append(temperatura)

    # Agregar las temperaturas de la nueva ciudad a la lista
    temperaturas.append(temperaturas_nuevas)


# Datos iniciales: Temperaturas de Lago Agrio, Quito y Portoviejo durante 4 semanas
temperaturas_ciudades = [
    [22.5, 23.1, 21.7, 22.0],  # Lago Agrio
    [18.0, 17.5, 19.0, 18.5],  # Quito
    [25.0, 24.5, 26.1, 24.8]  # Portoviejo
]

# Nombres de las ciudades
ciudades = ["Lago Agrio", "Quito", "Portoviejo"]

# Llamar a la función para agregar una nueva ciudad
agregar_nueva_ciudad(temperaturas_ciudades, ciudades)

# Calcular los promedios actualizados
promedios = calcular_promedio_temperaturas(temperaturas_ciudades, ciudades)

# Imprimir los promedios finales
print("Resumen de promedios:")
for i, promedio in enumerate(promedios):
    print(f"{ciudades[i]}: {promedio:.2f}°C")
