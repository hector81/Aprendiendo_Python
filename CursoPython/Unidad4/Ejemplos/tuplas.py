tupla = (4, "tu", 6.98, [1, 2])
print(tupla)

#slicing
tupla[2] # devuelve tercer elemento
print(tupla[2])
tupla[-1] # me devuelve la lista que hay en el ultimo elemento
print(tupla[-1])
tupla[-1][0] # me devuelve el primer elemento que hay en la lista que hay en el ultimo elemento
print(tupla[-1][0])

''' acceder por indices, por 2 o 3 indices o mas '''
# Por dos indices, que es desde donde hasta donde descontando la ultima posicion

# Por tres indices, que es desde donde hasta donde y en salto de 1,2 3, etc

print(tupla[:4:2]) # los 4 primeros elementos en saltos de dos

# Agregar un elemento a una tupla
x = 5, # esto seria una tupla, como si escribieras x = (5)
print(x)
y = 7, 8,
print(y)

x = x + tupla
print(x) # me devuelve una tupla con los elementos de ambas tuplas

ejemplo1 = (1,2)
ejemplo2 = (3,4)
ejemplo3 = ejemplo1 + ejemplo2
print(ejemplo3)




z = x + (7,)
print(z)

# ERRORES
#si intento añadir un entero a una tupla me dará error
# ERROR x = x + 7

