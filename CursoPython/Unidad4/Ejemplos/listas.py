lista = [1,2,3,4,5,6,7,8,9,10]
print(lista) # devuelve una lista
cumpleyears = ["Miercoles",28,"Diciembre",1983]
print(cumpleyears) # devuelve una lista
''' Listas pueden contener listas  '''
peliculas = [["El milagro de P tinto", 1998], ["Airbag", 1997]]
print(peliculas[0]) # primer elemento
print(peliculas[0][1]) # segundo elemento del primer elemento


''' Todos sus elementos del mismo tipo  '''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(lista)
diasLaborables = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
print(diasLaborables)

''' Elementos de tipos distintos '''
Cumpleanos = ["Martes", 28, "Diciembre", 1983]
print(Cumpleanos)

''' Muchos niveles de anidamiento '''
directores = [ ["Javier Fesser", ["El milagro de P tinto", 1998]], ["Juanma Bajo Ulloa", ["Airbag", 1997] ]]

print(directores[0]) # primer elemento
print(directores[0][1]) # segundo elemento del primer elemento
print(directores[0][1][0]) # primer elemento del segundo elemento del primer elemento