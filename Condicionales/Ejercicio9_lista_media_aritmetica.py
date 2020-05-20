'''
 2. Recibe una lista de
  enteros y calcula la media aritmetica (Fichero for-09-vacio.py).
'''
enteros = [1, 5, 9, 12, 13, 19, 23, 27, 29, 30, 57, 59, 67, 83, 92, 98, 100]
mediaAritmetica1 = sum(enteros) / len(enteros)
print(mediaAritmetica1)


mediaAritmetica2 = 0
suma = 0
contador = 0
for numero in enteros:
    suma += numero
    contador += 1

mediaAritmetica2 = suma / contador
print(mediaAritmetica2)
