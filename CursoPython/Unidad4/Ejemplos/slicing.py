''' slicing '''
lista = ['abc', 45, 3.52, 'dc', 30]
print(lista)
print(lista [1]) # acceder primer elemento
print(lista [-2]) # acceder penultimo elemento
print(lista [-2]) # acceder pultimo elemento

''' Acceder rangos '''
print(lista[1::4]) # accede desde el 1º elemento hasta el 3, el 4 no
print(lista[1::]) # accede desde el 1º elemento hasta el ultimo elemento
print(lista[::3]) # accede desde el 0º elemento hasta el 2º elemento

''' modificar las listas '''
lista[3] = 40 # modifica el 2º elemento
print(lista)
lista = [20, 40, 50, 30, 70, 65, 80, 90, 35] # modificamos o asignamos una lista nueva
print(lista)

''' saltos '''
lista[:9:2] # devolvería hasta el elemento 9 los impares de posición
print(lista[:9:2])
# esto sería otroa forma de hacerlo
lista[::2] # lo que haría es lo mismo, coger impares hasta el final sin marcarle hasta donde debe seguir
print(lista[::2])

#saltos de 3 en 3
print(lista[::3])

''' invertir lista entera '''
print(lista[::-1])

#modificar listas anidadas
lista = [123, '0abc', [50, 70], 4.67]
print(lista)
print(lista[2])

lista[2][1] = "string" # dentro del tercer elemento, modifica su segundo elemento
print(lista)
print(lista[2][1])