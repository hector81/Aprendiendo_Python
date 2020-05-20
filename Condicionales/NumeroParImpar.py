numeroPoner = 0
# bucle para poner numero correto
while numeroPoner < 1:
    # ponemos el numero
    numeroPoner = int(input('Escribe el número '))
    if numeroPoner < 1:
        print('El número debe ser positivo y mayor que 0')

if numeroPoner % 2 == 0:
    print('El número es par')
else:
    print('El número es impar')
