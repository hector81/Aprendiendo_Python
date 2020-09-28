''' funciones_listas '''
x = [20, 30, 40, 50, 30]
y = [20, "abc", 56, 90, "ty"]

print(len(x)) # devuelve numero elemento lista x

print(len(y)) # devuelve numero elemento lista x

#max y min solo funcionan con listas numéricas
print(max(x)) # maximo de la lista x

# ERROR # print(max(y)) # maximo de la lista y

print(min(x)) # MINIMO de la lista x

# ERROR # print(min(y)) # MINIMO de la lista y

''' FUNCION SUMA funcionan con listas numéricas '''
print(sum(x)) # sumaria todos los elementos de la lista x

# ERROR # print(sum(y)) # sumaria todos los elementos de la lista y

''' OPERADORES Y CONCATENADORES '''
c = x + y # me devuelve la concatenacion de ambas listas
print(c)

d = x * 3 # me devuelve 3 veces la misma lista en una sola lista
print(d)

''' BUSQUEDA in devuelve valores booleanos'''
print(23 in  x)# me pregunta si 23 está en la lista x, y devuelve true o false
print(30 in  x)# me pregunta si 23 está en la lista x, y devuelve true o false