'''
2. Importe el módulo del ejercicio1 en el siguiente código, de forma que las
instrucciones siguientes se ejecuten sin producir errores

a, b = 13, 3
print( (f'Operandos = {a},{b}')
print( (f'sumar => f'sumar => {operaciones_basicas.sumar(a, b)})
print( (f'restar => f'sumar => {operaciones_basicas.restar(a, b)})
print( (f'multiplicar => f'sumar => {operaciones_basicas.multiplicar(a, b)})
print( (f'dividir => f'sumar => {operaciones_basicas.dividir(a, b)})

¿Cómo debería importar el módulo para que no hubiera errores al ejecutar

a, b = 13, 3
print( (f'Operandos = {a},{b}')
'''
# PRIMERA FORMA
import Ejercicio1_operaciones_basicas

a, b = 13, 3
print(f'Operandos = {a},{b}')
print(f'sumar => {Ejercicio1_operaciones_basicas.sumar(a, b)}')
print(f'restar => {Ejercicio1_operaciones_basicas.restar(a, b)}')
print(f'multiplicar => {Ejercicio1_operaciones_basicas.multiplicar(a, b)}')
print(f'dividir => {Ejercicio1_operaciones_basicas.dividir(a, b)}')

# SEGUNDA FORMA
import Ejercicio1_operaciones_basicas as opBasic

a, b = 13, 3
print(f'Operandos = {a},{b}')
print(f'sumar => {opBasic.sumar(a, b)}')
print(f'restar => {opBasic.restar(a, b)}')
print(f'multiplicar => {opBasic.multiplicar(a, b)}')
print(f'dividir => {opBasic.dividir(a, b)}')

# TERCERA FORMA
from Ejercicio1_operaciones_basicas import *

a, b = 13, 3
print(f'Operandos = {a},{b}')
print(f'sumar => {sumar(a, b)}')
print(f'restar => {restar(a, b)}')
print(f'multiplicar => {multiplicar(a, b)}')
print(f'dividir => {dividir(a, b)}')
