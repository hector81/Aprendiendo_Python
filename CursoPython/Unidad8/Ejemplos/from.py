# importo las funciones que me interesan del modulo calculadora
from calculadora import suma
suma(11,9)
from calculadora import resta
resta(11,9)
from calculadora import multiplica
multiplica(11,9)
from calculadora import divide
divide(11,9)

print('******************')
# importo las funciones que me interesan del modulo calculadora y les asigno un nombre de variable
from calculadora import suma as SU
SU(11,10)
from calculadora import resta as RE
RE(11,10)
from calculadora import multiplica as MU
MU(11,10)
from calculadora import divide as DI
DI(11,10)

print('******************')
# no es recomendable porque puede tardar mucho en importarlo todo. Importa todo, funciones, metodos, etc
from calculadora import *

suma(32,91)
resta(32,1)
multiplica(32,2)
divide(32,4)
