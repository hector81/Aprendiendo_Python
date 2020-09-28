lista = ['abc  ',  45,  3.52,  'dc'  ,  30]
print(lista)
lista[1:4] # Celdas 1 a 3  (con el rango no se incluye el extremo final) 
print(lista[1:4])

lista[1] # Al buscar un elemento, devuelve un elemento
print(lista[1])

lista[1:2]#Al buscar un rango, devuelve una lista
print(lista[1:2])

lista[:4] #Elementos desde el primero hasta el 3
print(lista[:4])

lista[2:] #Elemento 2 hasta el final
print(lista[2:])

lista[:-3] # Elementos desde el primero hasta el -4
print(lista[:-3])

lista[-2:] # Elementos desde el penúltimo hasta el final
print(lista[-2:])

lista[:-1] # Todos los elementos menos el último
print(lista[:-1])

lista[1]=45 # Los elementos de una lista se pueden modificar, ahora el elemento 1 tiene un valor 45
print(lista[1])

lista  # La lista modificada
print(lista)   

lista=[20,40,50,30,70,65,80,90,35] # La hemos vuelto a modificar
print(lista)