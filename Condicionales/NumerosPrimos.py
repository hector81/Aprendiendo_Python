numero= int(input("¿Qué número quieres saber si es primo? "))

print('1 es primo')
print('2 es primo')
for x in range(3, numero):
    for i in range(2, x):
        if x%i != 0:
            #i no es divisor de x, x puede ser primo
            continue
        else:
            #i es divisor de x, x no es primo
            break #No es necesario buscar más divisores
    else:
        #El bucle for ha terminado con normalidad
        #El número que estábamos comprobando es primo
        print(str(x) + ' es primo')
