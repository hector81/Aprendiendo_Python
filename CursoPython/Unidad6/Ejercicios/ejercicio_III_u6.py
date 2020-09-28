'''
Escribe un programa que simule los lanzamientos de un dado. Muestre el resultado en cada
 lanzamiento y cuente la cantidad de intentos hasta que salga el número 6.
Para crear un numero aleatorio entre el 1 y el 6 se utiliza la siguiente sintaxis:
import random
x=random.randint(1, 6)
'''
import random # hay que importar la libreria
numero = 0 #inicializamos el numero a 0 para que no se cree un bucle infinito
contador = 0
while numero != 6: # mientras el número sea distinto de 6
    numero = int(random.randint(1, 6)) # generamos numero aleatorio entre el 1 y el 6
    contador+=1
    if numero == 6: # si el dado es igual a 6
        print(f"El dado ha salido {numero} y se ha acabado la partida.")
    else:
        print(f"El dado ha salido {numero}.")

print (f"Tu dado ha sacado un 6 a la {contador}º tirada")


