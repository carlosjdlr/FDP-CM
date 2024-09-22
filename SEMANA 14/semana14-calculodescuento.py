# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=15):
    """
    Calcula el descuento basado en el monto total y el porcentaje de descuento.

    :param monto_total: El monto total de la compra.
    :param porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto 15%).
    :return: El monto del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Función para mostrar el resultado final
def mostrar_resultado(monto_total, porcentaje_descuento=15):
    descuento = calcular_descuento(monto_total, porcentaje_descuento)
    monto_final = monto_total - descuento
    resultado = {
        "monto_total": monto_total,
        "porcentaje_descuento": porcentaje_descuento,
        "monto_descuento": descuento,
        "monto_final": monto_final
    }
    return resultado
