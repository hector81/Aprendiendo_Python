from io import open
archivo = open("Unidad10\\Ejemplos\\archivo.txt","bw", encoding="utf-8")
texto = "\n\nHola mundo"
archivo.write(texto)
# En el caso de que el archivo no exista en la carpeta donde lo estamos llamando, Python lo crea.
# escribir y leer archivo

dato = archivo.read()
print(dato)


archivo.close()
