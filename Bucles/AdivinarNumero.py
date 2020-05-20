# adivinar el numero de 0 a 100 con 10 intentos
import random

print('Adivina el numero de 0 a 100. Como pista te diremos si es mayor o menor')

numeroAleatorio = random.randint(1, 100)
miNumero = 0
numeroIntentos = 10
intentoActual = 0
# bucle para poner numeros
while numeroIntentos > 0:
    intentoActual = intentoActual + 1
    print('Intento numero ' + str(intentoActual))
    # ponemos el numero
    miNumero = int(input('Escribe el numero '))
    if numeroAleatorio == miNumero:
        print('Has acertado. El número era ' + str(numeroAleatorio))
        numeroIntentos = 0

    elif numeroAleatorio != miNumero:
        print('El número no es correcto')
        numeroIntentos = numeroIntentos - 1
        if miNumero > numeroAleatorio:
            print("El número es mayor al correcto ")
        elif miNumero <  numeroAleatorio:
            print('El número es menor al correcto')

    if numeroIntentos == 0:
        print('No has acertado. El número era ' + str(numeroAleatorio))
