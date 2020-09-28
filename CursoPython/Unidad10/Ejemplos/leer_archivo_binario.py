from io import open
archivo = open("Unidad10\\Ejemplos\\tiger.bmp", "bw")
#  archivo = open("archivo.bin", "bw")
dato = archivo.read()
print(dato)
archivo.close()