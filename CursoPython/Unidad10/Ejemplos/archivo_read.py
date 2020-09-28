# Si el archivo se encuentra en modo de lectura, lo lee y devuelve el contenido del archivo desde la posición en la que se encuentre hasta el final del archivo. Si se introduce un número como argumento,
#  lee el número de posiciones indicadas en el argumento.
f = open("Unidad10\\Ejemplos\\archivo.txt", "r")
print(f.read())