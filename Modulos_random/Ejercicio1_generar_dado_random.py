'''
EJERCICIOS
MÓDULO random
1. Cree un programa que simule el lanzamiento de un dado. Lance el dado un millón de veces. ¿Está tarado?
'''
import random

lanzamientosDados = 0
resultado1 = 0
resultado2 = 0
resultado3 = 0
resultado4 = 0
resultado5 = 0
resultado6 = 0

# bucle para poner numeros
while lanzamientosDados < 1000000:
    resultadoDadoAleatorio = random.randint(1, 6)
    print(f"Dado lanzado por {(lanzamientosDados + 1)} vez. Resultado = {resultadoDadoAleatorio}")
    lanzamientosDados += 1
    if resultadoDadoAleatorio == 1:
        resultado1 += 1
    elif resultadoDadoAleatorio == 2:
        resultado2 += 1
    elif resultadoDadoAleatorio == 3:
        resultado3 += 1
    elif resultadoDadoAleatorio == 4:
        resultado4 += 1
    elif resultadoDadoAleatorio == 5:
        resultado5 += 1
    elif resultadoDadoAleatorio == 6:
        resultado6 += 1

print(f"Ha salido el 1 = {resultado1} veces")
print(f"Ha salido el 2 = {resultado2} veces")
print(f"Ha salido el 3 = {resultado3} veces")
print(f"Ha salido el 4 = {resultado4} veces")
print(f"Ha salido el 5 = {resultado5} veces")
print(f"Ha salido el 6 = {resultado6} veces")
