x=5  # x es un entero
print(x)

x=5,   #x es una tupla (la coma hace la diferencia)
print(x)

#x=x+(7)
# TypeError: solamente se pueden concatenar tuplas a tuplas

x=5,
x=x+(7,)   #Concatenación correcta
print(x)  #x es una tupla
