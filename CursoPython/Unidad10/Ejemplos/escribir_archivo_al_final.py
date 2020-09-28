from io import open
# 'a' es un modo de escritura. En caso de existir un archivo, comienza a escribir al final de este.
fichero = open("Unidad10\\Ejemplos\\archivo2.txt", "a")
texto = "\n Esto es la linea final."
fichero.write(texto)
fichero.close()