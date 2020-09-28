# Recibe una lista como elemento a escribir en el archivo donde cada elemento 
# de la lista es una línea del documento

f = open("Unidad10\\Ejemplos\\archivo.txt", "a")
f.writelines(["See you soon!", "Over and out."])
f.close()

#open and read the file after the appending:
f = open("Unidad10\\Ejemplos\\archivo.txt", "r")
print(f.read())