# Devuelve el contenido del documento como una lista donde se encuentran todas las líneas del archivo
fichero = open("Unidad10\\Ejemplos\\archivo.txt", "r")
lista_lineas = fichero.readlines()
print(lista_lineas)
fichero.close()