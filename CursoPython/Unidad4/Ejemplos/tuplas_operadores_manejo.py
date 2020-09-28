# Operador de concatenación de tuplas.

a = (23,45,28)
b = (52,19)
c = a + b
print(c)

# Operador de reproducción de tuplas.

d = 3 * b
print(d)

# in / not in      Operador de inclusión. Sirve para comprobar si determinado valor está 
# incluido o no en una tupla. Es muy interesante para utilizarlo en condicionales, porque 
# su resultado es verdadero o falso.

tupla = (23, 45, 28, 52, 19)
print(23 in tupla)
print(2322 in tupla)