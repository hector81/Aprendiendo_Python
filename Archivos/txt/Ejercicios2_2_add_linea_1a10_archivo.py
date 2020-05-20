
'''
EJERCICIOS Manipulación de ficheros utilizando el intérprete Fichero "datos_ficheros"
********************************************************
2. Añadir la línea [1, 2 ... 10] a "datos_fichero" (¡no sobreescribas!)
********************************************************
'''
# funciones
def addArchivoLinea1a10(rutaEntrada):
    lineaAdd = ""
    for i in range(1,11):
        lineaAdd += str(i) + " , "
    lineaFinal = lineaAdd[0:(len(lineaAdd) - 3)] # para quitarle la ultima coma
    with open(rutaEntrada, "a", encoding="utf8") as archivo:
        archivo.write(lineaFinal + "\n")
    print(f"Linea añadida al final del archivo '{rutaEntrada}'")

# variables
rutaEntrada = "datos_fichero.txt"
# operaciones
addArchivoLinea1a10(rutaEntrada)
