columnas = int(input('Escribe el número de columnas:'))
filas = int(input('Escribe el número de filas:'))
while filas < 1 or columnas < 1:
    print('No empezamos bien... para dibujar un rectángulo no puedo usar números negativos')
    columnas = int(input('Escribe el número de columnas:'))
    filas = int(input('Escribe el número de filas:'))
for i in range(1, filas + 1):
    for j in range(1, columnas + 1):
        print ('*', end = '')
    print('')