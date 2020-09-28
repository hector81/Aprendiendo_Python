numero = int(input('¿De que número quieres saber su tabla de multiplicar? '))
for i in range(1,11):
    resultado = numero * i
    print(numero, ' x ', i, ' es igual a:', resultado)