'''
ORDENACIÓN DE LISTAS
'''
x = [8, 2, 3, 7, 5, 3, 7, 3, 1]
print(x)

print(f"1. El mayor número de la lista ")
print(f"{max(x)}")

print(f"2. El menor número de la lista ")
print(f"{min(x)}")

print(f"3. Los tres mayores números de la lista ")
lista = sorted(x, reverse=True)
print(lista[0:3])

print(f"4. El mayor de los tres primeros números de la lista")
print(f"{max(x)}")

print(f"5. El menor de los cuatro últimos números de la lista ")
print(f"{min(x[len(x)-4:len(x)])}")

print(f"6. La suma de los cinco mayores números de la lista ")
print(f"{sum(lista[0:5])}")

print(f"7. La suma de los tres menores números de la lista")
print(f"{sum(x[len(lista)-3:len(lista)])}")
print(lista)
