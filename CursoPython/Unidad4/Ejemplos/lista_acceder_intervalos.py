lista = ['abc  ',  45,  3.52,  'dc'  ,  30]

lista[0:9:2] # El tercer índice indica el incremento (cada dos[20, 50, 70, 80, 35]elementos)
print(lista[0:9:2])

lista[0:-1:2]   # desde el índice 0 hasta el final ( sin contar el último) de dos en dos
print(lista[0:-1:2])

lista[::2] # toda la lista con intervalos de 2
print(lista[::2])

lista[::3] # toda la lista con intervalos de 3
print(lista[::3])

lista[::-1]  # Esta notación especial invierte la lista
print(lista[::-1])