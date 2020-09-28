'''
La función shuffle() 'mezcla' o cambia aleatoriamente el orden de los elementos de una lista antes
 de realizar la selección de alguno de ellos. Esta mezcla recuerda en el caso de los juegos de cartas 
 la acción de barajar un número de veces antes de repartir o seleccionar cartas.
'''
import random

mylist = ["1 de picas", "2 de picas", "3 de picas", "4 de picas", "5 de picas", "6 de picas"]
random.shuffle(mylist)

print(mylist)
