# Una vez que se hayan realizado todas las operaciones en un archivo, debemos cerrarlo de manera 
# adecuada. En caso de no hacerlo, es altamente probable que el archivo se encuentre en un estado 
# inestable y corra riesgo de que la información contenida se corrompa o destruya.
fichero = open("Unidad10\\Ejemplos\\archivo.txt", "w")
texto = "Línea 1\nLínea 232423\nLínea 3\nLínea 4" + " esto es una nueva linea"
fichero.write(texto)
fichero.close()