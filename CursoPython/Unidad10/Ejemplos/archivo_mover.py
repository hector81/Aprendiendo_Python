from io import open
import os
#creamos archivo y comprobamos que exista
archivo = open('Unidad10\\Ejemplos\\archivo447.txt', 'w')
os.path.isfile('Unidad10\\Ejemplos\\archivo447.txt')

# hay que cerrarlo antes de mover 
archivo.close()
# lo movemos
os.rename('Unidad10\\Ejemplos\\archivo447.txt','Unidad10\\Ejemplos1\\archivo448.txt')
os.path.isfile('Unidad10\\Ejemplos\\archivo448.txt')