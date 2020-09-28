'''
La función randrange(a, b, c) genera un número entero entre los valores generados por range(a, b, c). 
Como ocurre con range(), la función randrange() admite uno, dos o tres argumentos.
'''
import random

print(random.randrange(10)) # da un valor aleatorio entre 0 y 10

print(random.randrange(1, 90)) # da un valor aleatorio entre 1 y 90
 
print(random.randrange(10, 200, 10)) # da un valor aleatorio entre 10 y 200, con saltos de 10
# esto quiere decir que dara los siguientes valores : 10 ,20,30,40,50,60,70,80,90,100,110,120,130 hasta 200
