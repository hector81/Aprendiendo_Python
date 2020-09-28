#No puedes iterar ninguna colección como si fuera una secuencia. Sin embargo, hay una función muy interesante
#  que permite convertir las cadenas y algunas colecciones a iteradores, la función iter():

lista = [1,2,3,4,5]
lista_iterable = iter(lista)
print(next(lista_iterable)) # posicion 0
print(next(lista_iterable)) # posicion 1
print(next(lista_iterable)) # posicion 2
print(next(lista_iterable)) # posicion 3
print(next(lista_iterable)) # posicion 4
 # no se puede mas posiciones o dará error

# es lo mismo que :
for i in lista:
    print(i)