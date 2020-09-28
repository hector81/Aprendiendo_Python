# La diferencia entre una función normal y una generadora es que mientras una instrucción
#  return termina una función por completo, la instrucción yield pausa la función
#  guardando todos sus estados y luego continúa desde allí en llamadas sucesivas.

def pares(numero):
    for n in range(numero+1):
        if n % 2 == 0:
            yield n

for numero in pares(10):
    print(numero)

print(pares(10))


