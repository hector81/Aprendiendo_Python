'''
5. A partir de dos listas de enteros, 'numeros1' y 'numeros2', crea una lista que contiene
aquellos valores de la primera que tambien estan en la segunda e imprimela por pantalla.
 Es decir, calcula la interseccion de ambas listas. (Fichero for-05-vacio.py
'''
numeros1 = [1, 7, 13, 21, 27, 29, 34, 48, 50, 51, 53, 61, 68, 74, 82, 83, 84, 87, 92, 94]
numeros2 = [4, 6, 10, 18, 23, 29, 30, 32, 43, 54, 55, 55, 71, 76, 77, 82, 88, 92, 94, 95]


listaMultiplicacion_interseccion = []
for x, y in zip(numeros1, numeros2):
    listaMultiplicacion_interseccion.append(x * y)
print(f'Interseccion listas = {listaMultiplicacion_interseccion}')
