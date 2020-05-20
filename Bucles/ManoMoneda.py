 # El programa simulará el juego de adivinar en qué mano está la moneda.
 # Le preguntará a la persona el nombre y cuantas partidas quiere jugar,
 # luego calculará el ganador.
import random

def introducirNumero():
     while True:
         try:
             numeroVecesPartida = int(input("Por favor ingrese un número : "))
             if numeroVecesPartida > 0:
                return numeroVecesPartida
                break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

print("Por favor ingrese un número de partidas: ")
numeroVecesPartida = introducirNumero()

while numeroVecesPartida > 0:
    print('¿En que mano tengo la moneda? Si crees que en la derecha pulsa 1 y si es en la izquierda pulsa 2')
    numeroEleccion = int(input("Escoge la mano : "))
    if numeroEleccion > 2 or numeroEleccion < 1:
            print('Tienes que poner 1:derecha o 2:izquierda. No valen otros numeros')
    else:
        numeroAleatorio = random.randint(1, 2)
        if numeroAleatorio == numeroEleccion:
            print('Has acertado')
            numeroVecesPartida = 0
        else:
            if (numeroVecesPartida - 1) == 0:
                print('No has acertado y ya no quedan intentos')
                numeroVecesPartida = 0
            else:
                print('No has acertado. Vuelve a intertarlo. Te quedan ' + str(numeroVecesPartida - 1) + ' intentos')
                numeroVecesPartida = numeroVecesPartida - 1
