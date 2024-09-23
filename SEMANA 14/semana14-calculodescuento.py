def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento y el monto final de una compra.
    Parámetros:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float): El porcentaje de descuento a aplicar. Valor predeterminado es 10%.

    Retorna:
        tuple: Descuento calculado y monto final después del descuento.
    """
    try:
        if monto_total < 0 or porcentaje_descuento < 0:
            raise ValueError("El monto total y el porcentaje de descuento deben ser números positivos.")
        descuento = (porcentaje_descuento / 100) * monto_total
        monto_final = monto_total - descuento
        return descuento, monto_final
    except TypeError:
        print("Error: Asegúrate de ingresar números válidos.")
        return None, None
def mostrar_resultado(descuento, monto_final):
    """
    Muestra los resultados del cálculo de descuento y monto final.
    Parámetros:
        descuento (float): El monto descontado.
        monto_final (float): El monto final después de aplicar el descuento.
    """
    if descuento is not None and monto_final is not None:
        print(f"\nMonto del descuento: ${descuento:.2f}")
        print(f"Monto final a pagar después del descuento: ${monto_final:.2f}")
    else:
        print("No se pudo realizar el cálculo.")
def ingresar_monto():
    """
    Solicita al usuario que ingrese el monto total de la compra.

    Retorna:
        float: El monto total ingresado por el usuario.
    """
    while True:
        try:
            monto = float(input("Ingresa el monto total de la compra: $"))
            if monto < 0:
                raise ValueError("El monto debe ser un número positivo.")
            return monto
        except ValueError as e:
            print(f"Error: {e}. Intenta nuevamente.")
def ingresar_descuento():
    """
    Solicita al usuario que ingrese el porcentaje de descuento o permite usar el valor predeterminado.

    Retorna:
        float: El porcentaje de descuento ingresado por el usuario o el valor predeterminado de 10%.
    """
    while True:
        try:
            descuento = input("Ingresa el porcentaje de descuento (presiona Enter para usar el 10% predeterminado): ")
            if descuento == "":
                return 10  # Valor predeterminado
            descuento = float(descuento)
            if descuento < 0:
                raise ValueError("El porcentaje de descuento debe ser un número positivo.")
            return descuento
        except ValueError as e:
            print(f"Error: {e}. Intenta nuevamente.")
def menu():
    """
    Muestra un menú interactivo y permite al usuario calcular descuentos múltiples veces.
    """
    while True:
        print("\n--- Calculadora de Descuentos ---")
        print("1. Calcular descuento usando el 10% predeterminado")
        print("2. Calcular descuento ingresando un porcentaje personalizado")
        print("3. Salir")
        opcion = input("Elige una opción (1, 2, o 3): ")
        if opcion == "1":
            monto_total = ingresar_monto()
            descuento, monto_final = calcular_descuento(monto_total)
            mostrar_resultado(descuento, monto_final)
        elif opcion == "2":
            monto_total = ingresar_monto()
            porcentaje_descuento = ingresar_descuento()
            descuento, monto_final = calcular_descuento(monto_total, porcentaje_descuento)
            mostrar_resultado(descuento, monto_final)
        elif opcion == "3":
            print("Saliendo del programa. ¡Gracias!")
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")
if __name__ == "__main__":
    menu()