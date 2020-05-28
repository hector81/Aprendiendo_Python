'''
LISTAS Manipulación de listas utilizando el intérprete
'''
lista = ["primero",2,"3.5",4.0,"ultimo"]
print(lista)
print(f"1. ¿El tamaño de la lista?")
print(len(lista))

print(f"2. El tamaño de la lista multiplicado por su segundo elemento .")
print(f"{len(lista)} x {lista[1]} = {(len(lista)*lista[1])}")

print(f"3. El producto del segundo elemento de la lista por el tercero. ")
print(f"{lista[1]} ** {lista[2]} = {(lista[1] ** float(lista[2]))}")

print(f"4. ¿Está 2 en la lista? ¿Y 2.0? ")
boolComp1 = False
boolComp2 = False
for elemento in lista:
    elementoSTR = str(elemento)
    if elementoSTR == "2":
        boolComp1 = True
    if elementoSTR == "2.0":
        boolComp2 = True
if boolComp1 == True:
    print(f"2 está en la lista")
else:
    print(f"2 no está en la lista")
if boolComp2 == True:
    print(f"2.0 está en la lista")
else:
    print(f"2.0 no está en la lista")

print(f"5. Eliminar el primer elemento de la lista.")
lista.pop(0)
print(lista)

print(f"6. Eliminar ahora los dos últimos elementos simultaneamente. ")
del lista[len(lista)-2:len(lista)]
print(lista)

print(f"7. ¿Está la lista vacía? ")
if len(lista) == 0:
    print(f"La lista está vacía")
else:
    print(f"La lista no está vacía")

print(f"8. Añadir el elemento 'nuevo ultimo' a la lista.")
lista.append('nuevo ultimo')
print(lista)
