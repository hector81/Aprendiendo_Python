'''
CONJUNTOS Y DICCIONARIO
'''
x = [8, 2, 3, 2, 2]
y = [8, 2, 3, 2, 9]

print(f"1. ¿Cuántos elementos hay en x si se eliminan los repetidos? ")
listaSinDuplicadosX = list(set(x))
print(f'{len(listaSinDuplicadosX)}')

print(f"2. Una lista que contenga la concatenación de ambas listas. ")
a = set(x)
b = set(y)
# listaExtendida = a.union(b)
listaExtendida = x + y
print(f'{listaExtendida}')

print(f"3. Una lista que contenga la unión de ambas listas, sin duplicados. ")
ListaExtendidaSinDuplicados = list(set(listaExtendida))
print(f'{ListaExtendidaSinDuplicados}')

print(f"4. Un conjunto que tenga la intersección de ambas listas. ")
x1 = set(x)
y1 = set(y)
listaInterseccion = x1.intersection(y1)
print(f'{listaInterseccion}')

print(f"5. Un diccionario en el que para cada entero de la lista x se almacena su cuadrado. ")
diccionario = {}
for numero in listaSinDuplicadosX:
    diccionario[numero] = numero * numero
print(diccionario)

print(f"6. Un diccionario en el que se almacena el número de veces que cada entero aparece en la lista y.")
for numero in y:
    repetidos = y.count(numero)
    diccionario[numero] = numero
    print(f'{numero} = {repetidos}')

print(diccionario)
