# Crear un Diccionario
informacion_personal = {
    "nombre": "Carlos Macias",
    "edad": 19,
    "ciudad": "Lago Agrio",
    "profesion": "Ingeniero"
}

# Acceder y Modificar Valores
# Accedemos al valor de la clave "ciudad" y lo modificamos
informacion_personal["ciudad"] = "Portoviejo"

# Agregar una nueva clave-valor
# Actualizamos el valor de la clave "profesion"
informacion_personal["profesion"] = "Doctor"

# Verificar Existencia de Claves
# Verificamos si la clave "telefono" existe, si no, la agregamos
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar una Clave
# Eliminamos la clave "edad"
informacion_personal.pop("edad", None)  # Utilizamos pop para eliminar la clave de manera segura

# Imprimir el Diccionario Final
print("Diccionario final:")
print(informacion_personal)
