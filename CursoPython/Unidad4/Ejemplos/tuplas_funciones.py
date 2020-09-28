x=(20,30,45,50,30)
print(x)

print(len(x)) # Longitud o cantidad de elementos en una tupla.

print(max(x)) # El mayor valor dentro de una tupla.

print(min(x)) # El menor valor dentro de una tupla.

print(sum(x)) # Suma de componentes dentro de una tupla.

#Una tupla se puede convertir a lista.

x = ('abc',  73,  5.28,  'rs',  5)
x = list(x)
print(x[1])
print(x) 


# Una lista se puede convertir a tupla.

x = ['abc',  73,  5.28,  'rs',  5]
x = tuple(x)
print(x)


# Los valores de una tupla se pueden distribuir (desempaquetar) asignando a variables .
t = (34, 25, 42)
a,b,c = t
print(a)
print(b)
print(c)

# Una función para formar tuplas entre dos listas: zip (devuelve una lista de tuplas).
c=[101,231,725]
m=['Algebra','Física','Química']
p=zip(c,m)
list(p)
print(p)


# Error: max, min solo son aplicables con tuplas numéricas.
# max(x)
# TypeError: unorderable tuple: str() > int()

# Error: sum solo aplicable a tuplas numéricas.
# sum(x)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'