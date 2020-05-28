'''
EJERCICIOS MÓDULO math
1. Determine el logaritmo decimal de los 1000 primeros números enteros. Guarde
el resultado en un fichero cuyas filas tendrán el siguiente formato 'x y',
donde x será el entero e y su correspondiente logaritmo decimal.
'''
import math

diccionarioLogaritmo = {}
for i in range(1, 1001):
    diccionarioLogaritmo[i] = math.log10(i)

with open('logaritmosDecimales_numeros1000.txt', 'w') as archivo:
    archivo.write(f"NOTA = X será el entero e Y su correspondiente logaritmo decimal\n")
    for elemento in diccionarioLogaritmo:
        archivo.writelines(f"x = {elemento} . y = {diccionarioLogaritmo[elemento]}\n")
