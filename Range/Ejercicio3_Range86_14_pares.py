'''
3. Imprime por pantalla la secuencia [86, 84, 82 ... 14].
'''
listaPares = []
for numero in range(86, 13, -2):
    if numero%2 == 0:
        listaPares.append(numero)

print(f'Secuencia pares [86, 84, 82 ... 14] = {listaPares}')
