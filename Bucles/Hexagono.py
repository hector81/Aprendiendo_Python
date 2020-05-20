numero = 0
cuadrado = ''
# bucle para poner numero correto
while numero < 1 :
    # ponemos el numero
    numero = int(input('Escribe el número '))
    print()
    if numero < 1:
        print('El número debe ser positivo')
    else:
        numeroArriba = numero
        while numeroArriba < ((numero*2) + 3):
            for i in range(0, ((numero*2)-1)):
                if i < numero:
                    cuadrado = cuadrado + ' '
                else:
                    cuadrado = cuadrado + 'x'
            print(cuadrado)
            cuadrado = ''

            numeroArriba = numeroArriba + 2
