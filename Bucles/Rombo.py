# introducir altura rombo
alturaX = 0
# bucle para poner numero correto
while alturaX < 1:
    # ponemos el numero
    alturaX = int(input('Escribe la altura '))
    if alturaX < 1:
        print('El número debe ser positivo')
    else:
        for i in range(0, alturaX + 1):
            for j in range(alturaX - i):
                print(" ", end="")
            for j in range(i):
                print("* ", end="")
            print('\n')
        z = alturaX - 1
        while z > 0:
            for x in range(alturaX - z):
                print(" ", end="")
            for x in range(z):
                print("* ", end="")
            z = z - 1
            print('\n')
