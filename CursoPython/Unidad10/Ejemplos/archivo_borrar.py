from io import open
import os
#creamos archivo y comprobamos que exista
archivo = open('Unidad10\\Ejemplos\\archivo449.txt', 'w')
os.path.isfile('Unidad10\\Ejemplos\\archivo449.txt')

# hay que cerrarlo antes de mover 
archivo.close()
# lo borramos
os.remove('Unidad10\\Ejemplos\\archivo449.txt')
os.path.isfile('Unidad10\\Ejemplos\\archivo449.txt')