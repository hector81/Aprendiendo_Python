objeto = "Hola" # variable global
def funcion():
    objeto = 2 # variable local solo dentro de la funcion
    print(objeto)

funcion() # imprime variable local


print(objeto) # imprime variable global

'''
ESTO IMPRIMIRIA HOLA Y HOLA
objeto = "Hola" # variable global
def funcion():
    print(objeto)
funcion() # imprime variable global
print(objeto) # imprime variable global
'''