'''
2. Imprime por pantalla la secuencia [0, 2, 4 ... 200].
'''
listaPares = []
for numero in range(0,201):
    if numero%2 == 0:
        listaPares.append(numero)

print(f'Secuencia pares [0, 2, 4 ... 200] = {listaPares}')
