# Lectura de Archivo de Texto
# Abrimos el archivo 'my_notes.txt' en modo de lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos el archivo línea por línea utilizando un bucle
    for line in file:
        # Mostramos cada línea leída en la consola
        print(line.strip())  # strip() elimina los saltos de línea al final

# Al usar 'with', no es necesario cerrar el archivo manualmente, ya que se cierra automáticamente al salir del bloque.
