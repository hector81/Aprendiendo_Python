anchura = 0
altura = 0
cuadrado = ''
# bucle para poner numero correto
while altura < 1 or anchura < 1 :
    # ponemos el numero
    anchura = int(input('Escribe la anchura '))
    altura = int(input('Escribe la altura '))
    print()
    if altura < 1 or anchura < 1 :
        print('El número debe ser positivo')
    else:
        for i in range(0, altura):
            for j in range(anchura):
                cuadrado = cuadrado + 'x'
            print(cuadrado)
            cuadrado = ''
