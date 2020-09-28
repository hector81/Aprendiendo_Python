def pares(numero):
    lista = []
    for n in range(numero+1):
        if n % 2 == 0:
            lista.append(n)
    return (lista)

numero = int(input('Genera lista de números hasta el número: '))
print(pares(numero))