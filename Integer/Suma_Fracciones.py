# Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:

# 12,14,18,116,132,164,…
# en forma decimal:

# 0.5,0.25,0.125,0.0625,0.03125,0.015625,…
# El programa debe mostrar tres columnas que contengan la siguiente información:

# Potencia  Fraccion  Suma
# 1         0.5       0.5
# 2         0.25      0.75
# 3         0.125     0.875
# 4         0.0625    0.9375
# ...       ...       ...
# El programa debe terminar cuando la fracción decimal sea menor o igual a 0.0001.
potencia = 1
divisor = 1
fraccion = 0
fraccionC = 100
suma = 0
contador = 0
linea = 'Potencia  Fracción  Suma' + '\n'
while fraccionC > 0.0001:
    divisor = divisor * 2
    fraccion = potencia/divisor
    suma = suma + fraccion
    contador = contador + 1
    linea = linea + str(contador) + '      ' + str(fraccion) + '      ' + str(suma) + '\n'
    fraccionC = fraccion
print(linea)
