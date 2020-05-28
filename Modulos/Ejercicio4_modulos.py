'''
4. Cree un nuevo directorio en su directorio de usuario llamado modulos.
 Copie el modulo operaciones_basicas.py en dicho directorio.
 Haga lo necesario, en su código o en el sistema, para que se ejecute
 el apartado (a) del ejercicio 2 desde cualquier otro directorio que no
  sea modulos.
'''
import sys
sys.path.append('C:\\xampp\\htdocs\\AprenderPython\\Ejercicios\\L7_Modulos')

import Ejercicio1_operaciones_basicas

a, b = 13, 3
print(f'Operandos = {a},{b}')
print(f'sumar => {Ejercicio1_operaciones_basicas.sumar(a, b)}')
print(f'restar => {Ejercicio1_operaciones_basicas.restar(a, b)}')
print(f'multiplicar => {Ejercicio1_operaciones_basicas.multiplicar(a, b)}')
print(f'dividir => {Ejercicio1_operaciones_basicas.dividir(a, b)}')
