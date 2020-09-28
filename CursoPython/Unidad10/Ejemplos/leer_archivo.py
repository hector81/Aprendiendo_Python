from io import open
# ruta1 = "archivo.txt"
# open(ruta1,"r") # modo lectura

fichero = open('Unidad10\\Ejemplos\\archivo.txt','r', encoding="utf-8")
dato = fichero.read()
print(dato)
fichero.close()