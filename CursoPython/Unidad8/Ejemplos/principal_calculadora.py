import calculadora
# Uso las funciones importadas
calculadora.suma(3,9)
calculadora.resta(3,9)
calculadora.multiplica(3,9)
calculadora.divide(3,9)

print('******************')
# igualo variables con las funciones importadas, y las uso como funciones directamente
suma = calculadora.suma
resta = calculadora.resta
multiplica = calculadora.multiplica
divide = calculadora.divide

suma(32,9)
resta(32,9)
multiplica(32,9)
divide(32,9)

print('******************')
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
