'''
1. Para cada una de las cadenas de texto almacenadas en una lista, imprimir por pantalla el
 indice y la cadena en si e indicar si la palabra es demasiado corta (cinco o menos caracteres)
 o larga (mas de cinco caracteres) (Fichero for-08-vacio.py).
'''


frase = "Programmers are, in their hearts, architects, and the first thing they want to do when they get to a site is to bulldoze the place flat and build something grand"

listado = frase.split(" ")

for posicion, palabra in enumerate(listado):
    if len(palabra) > 5:
        print(f"Palabra {(posicion+1)} = {palabra} . Es demasiado larga")
    else:
        print(f"Palabra {(posicion+1)} = {palabra} . Es demasiado corta")
