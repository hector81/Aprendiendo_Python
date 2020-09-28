# EJEMPLO: Distintas pruebas con los métodos de archivos
archivo = open("Unidad10\\Ejemplos\\archivo.txt","bw")
archivo.write(b'Hola Mundo')
# 10

# Si intentas leer el archivo, como lo has abierto en modo escritura te devolverá un error.
# archivo.read()
# Traceback (most recent call last):
 #  File "<stdin>", line 1, in <module>
# io.UnsupportedOperation: read

# Es posible recorrer el archivo, es decir: pasar por sus caracteres.
archivo.seekable()
# True

# Sabe dónde está el puntero.
archivo.tell()
# 10
# Reubicar el puntero dentro del archivo.
archivo.seek(3)
# 3
# Vuelvo a comprobar donde está el puntero.
archivo.tell()
# 3
# Abro de nuevo el archivo en modo lectura.
archivo = open("Unidad10\\Ejemplos\\archivo.txt","br")

# Leer desde donde se encuentre el puntero hasta 9 caracteres.
archivo.read(9)
# b'Hola Mund'
# Leer desde donde se encuentre el puntero hasta el final.
archivo.read()
# b'o'
# Recoloco el puntero en la posición 0.
archivo.seek(0)
# 0
# Leer desde donde se encuentre el puntero hasta el final.
archivo.read()
# b'Hola Mundo'

# Vuelvo a abrir el archivo en modo escritura tipo texto para pode usar writelines y readlines
archivo = open("Unidad10\\Ejemplos\\archivo.txt","w")
# Reescribo la primera linea
archivo.write("Hola Mundo")
# 10
# Añado otras dos lineas de texto a mi archivo
archivo.write("\n Queremos un mundo")
# 19
archivo.write("\n Donde quepan muchos mundos")
# 28
# Utilizo la función writelines para añadir 2 lineas más al archivo
archivo.writelines(['\n cuarta linea','\n quinta linea'])
# Reabro en forma lectura
archivo = open("Unidad10\\Ejemplos\\archivo.txt","r")
# Realiza diferentes pruebas con el método readlines
archivo.readline()
# 'Hola Mundo\n'
archivo.readline()
# ' Queremos un mundo\n'
archivo.readline()
# ' Donde quepan muchos mundos'
archivo.seek(0)
# 0
a = archivo.readlines()
# a
print(a)
# ['Hola Mundo\n', ' Queremos un mundo\n', ' Donde quepan muchos mundos\n', 'cuarta linea', 'quinta linea']

# anterior
  
# 2
 
# 3
