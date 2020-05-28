'''
EJERCICIOS
MÓDULO random
2. Cree un programa que simule el lanzamiento de dos dados. Lance esos dados 1000 veces.
 ¿cuantas veces ha obtenido una suma de dados igual a dos? ¿Cuantas veces ha obtenido
 una suma de dados igual a un número par?
'''
import random

lanzamientosDados = 0
dado1 = 0
dado2 = 0
suma2 = 0
sumaPar = 0

# bucle para poner numeros
while lanzamientosDados < 1000:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    lanzamientosDados += 1
    suma = dado1 + dado2
    if suma == 2:
        suma2 += 1
    elif suma%2 == 0:
        sumaPar += 1

print(f"Ha sumado dos en  = {suma2} veces")
print(f"Han sumado un numero par en = {sumaPar} veces")
