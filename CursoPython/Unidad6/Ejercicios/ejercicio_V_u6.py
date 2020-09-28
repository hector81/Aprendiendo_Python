'''
Diseña un programa que genere un entero al azar entre 1 y 10,  te permita introducir números para
 saber si aciertas dicho número. El programa debe incluir un mensaje de ayuda y un conteo
  de intentos.
'''
import random # hay que importar la libreria
numero = int(random.randint(1, 10)) # generamos numero aleatorio entre el 1 y el 10
contador = 0
booleano = False
while booleano == False: # mientras no cambie la condición
    numero_introducido = int(input("Introduce un número para ver si coincide con el aleatorio: "))
    contador += 1 # aumentamos el contador de intentos
    if numero_introducido != numero: # si es distinto al aleatorio
        print(f"El número {numero_introducido} no coincide con el correcto y tú número de intentos es de {contador}.")
    else:
        print(f"Enhorabuena, el {numero_introducido} era el correcto. Has realizado {contador} intentos en total.")
        booleano = True # cambiamos condición para salir del bucle
