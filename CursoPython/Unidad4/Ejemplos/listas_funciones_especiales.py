animales = ["Perro", "Gato", "Tigre", "Gallo", "Ratón"]
print(animales)

''' FUNCION APPEND '''
# agregamos elemento a la lista. Lo añade en el último lugar de la lista
animales.append("Periquito")
print(animales)

''' FUNCION INSERT '''
# podemos también agregar el elemento en una posición concreta de la lista
animales.insert(1,"Gorrión") # se añadira en la segunda posicion donde esta gato
print(animales)

''' FUNCION COUNT '''
# podemos contar cuantas veces aparece un elemento en la lista
print(animales.count("Gato"))
print(animales.count("León"))

''' FUNCION POP '''
# eliminamos elemento por indice
#animales.pop(2) # me elimina la tercera posicion, en este caso gato. Si ponemos print tambien lo imprime
print(animales.pop(2))
print(animales)
animales.pop(2) # en este caso no imprime pero elimina igualmente
print(animales)

''' FUNCION SORT '''
# organizar la lista ascendentemene por abecedario pero funcionaria para numeros
animales.sort()
print(animales)
numeros = [201, 30, 410, 50, 310]
numeros.sort()
print(numeros)

''' FUNCION REVERSE '''
# invertir el sentido de la lista
animales.reverse()
numeros.reverse()
print(animales)
print(numeros)

''' FUNCION CLEAR '''
# podemos limpiar la lista entera
animales.clear()
numeros.clear()
print(animales)
print(numeros)

''' FUNCION REMOVE '''
# podemos limpiar de una lista un elemento si se lo indicamos directamente
animales = ["Perro", "Gato", "Pez", "Tigre", "Gallo", "Ratón", "Pez"]
animales.remove("Gallo")
print(animales)
# si son varios iguales, solo elimina el primero que aparezca
animales.remove("Pez")
print(animales)

''' FUNCION INDEX '''
# Podemos buscar la posición de un elemento indicado
print(animales.index("Tigre"))
