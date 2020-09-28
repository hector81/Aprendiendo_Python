'''
La función choice(secuencia) elige un valor al azar en un conjunto de elementos. 
Cualquier tipo de datos enumerables (tupla, lista, cadena, range) puede utilizarse
 como conjunto de elementos.
'''
import random
#lista
print(random.choice(['win', 'lose', 'draw']))
#cadena
print(random.choice("estocadena"))
#tupla
print(random.choice(("Python", True, "Zope", 5)))
#range
print(random.choice(range(1, 150)))