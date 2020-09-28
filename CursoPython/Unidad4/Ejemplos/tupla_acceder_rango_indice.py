tupla = ('abc  ',  45,  3.52,  'dc'  ,  30)
print(tupla)

# tupla[1:4] # Celdas 1 a 3  (con el rango no se incluye el extremo final) 
print(tupla[1:4])
#(49, 3.52, 'dc')

#devuelve un elemento
print(tupla[1])
#devuelve una tupla
print(tupla[1:2])

#tupla[:4] #Elementos desde el primero hasta el 3
print(tupla[:4])
#('abc', 49, 3.52, 'dc')

#tupla[2:] #Elemento 2 hasta el final
print(tupla[2:])
#(3.52, 'dc', 30)

# tupla[:-3] # Elementos desde el primero hasta el -4
print(tupla[:-3])
#('abc', 49)

# tupla[-2:] # Elementos desde el penúltimo hasta el final
print(tupla[-2:])
#('dc', 30)

# tupla[:-1] # Todos los elementos menos el último
print(tupla[:-1])
#('abc', 49, 3.52, 'dc')


# tupla[1]=45 # Los elementos de una tupla no se pueden modificar
#TypeError: 'tuple' object does not support item assignment