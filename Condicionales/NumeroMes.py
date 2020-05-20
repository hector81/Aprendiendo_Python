numeroMes = 0
# bucle para poner numero correto
while numeroMes < 1 or numeroMes > 12:
    # ponemos el numero
    numeroMes = int(input('Escribe el número de mes '))
    if numeroMes < 1 or numeroMes > 12:
        print('El número debe ser entre 1 y 12')
    else:
        print('El número de mes corresponde a ')

if numeroMes ==  1:
    print('Enero ')
elif numeroMes ==  2:
    print('Febrero')
elif numeroMes ==  3:
    print('Marzo')
elif numeroMes ==  4:
    print('Abril')
elif numeroMes ==  5:
    print('Mayo')
elif numeroMes ==  6:
    print('Junio')
elif numeroMes ==  7:
    print('Julio')
elif numeroMes ==  8:
    print('Agosto')
elif numeroMes ==  9:
    print('Septiembre')
elif numeroMes ==  10:
    print('Octubre')
elif numeroMes ==  11:
    print('Noviembre')
elif numeroMes ==  12:
    print('Diciembre')
