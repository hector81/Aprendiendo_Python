x = (20, 30, 40, 50, 30)
print(x)

print(len(x)) #numero elementos tupla

print(max(x)) # el elemento mayor de la tupla

print(min(x)) # el elemento menor de la tupla


# convertir tupla a lista
y = list(x)
print(y)

# convertir lista a tupla
z = tuple(y)
print(z)

# desempaquetar una tupla
a,b,c,d,e = z
print(a)
print(b)
print(c)
print(d)
print(e)