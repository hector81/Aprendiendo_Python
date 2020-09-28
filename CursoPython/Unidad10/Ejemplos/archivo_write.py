#i el archivo se encuentra en modo de escritura, añadirá al archivo el contenido
#  ingresado como argumento a partir de la posición en donde se encuentre el cursor o puntero,
#  sobreescribiendo el texto existente si lo hay.
#  Una vez terminada la operación, regresará la nueva posición del puntero.

fichero = open("Unidad10\\Ejemplos\\archivo.txt", "w")
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4" + " esto es una nueva linea"
fichero.write(texto)
fichero.close()