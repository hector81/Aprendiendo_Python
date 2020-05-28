'''
EJERCICIOS MÓDULO math
2. Compruebe que el seno de 0º es 0, el de 90º 1 y el de 270º -1
'''
import math

print(f"¿Es el seno de 0º igual a 0?")
coseno0 = math.sin(0)
if coseno0 == 0:
    print(f"Si")
else:
    print(f"No, es {coseno0}")

print(f"¿Es el seno de 90ºº igual a 1?")
coseno90 = math.sin(90)
if coseno90 == 1:
    print(f"Si")
else:
    print(f"No, es {coseno90}")

print(f"¿Es el seno de 270º igual a -1?")
coseno270 = math.sin(270)
if coseno270 == -1:
    print(f"Si")
else:
    print(f"No, es {coseno270}")
