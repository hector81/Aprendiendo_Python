from io import open

# Creamos un fichero de prueba con 4 líneas
fichero = open("Unidad10\\Ejemplos\\archivo2.txt", "w")
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4" + " esto es una nueva linea"
fichero.write(texto)
fichero.close()

