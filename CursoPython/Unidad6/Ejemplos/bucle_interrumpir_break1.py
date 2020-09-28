import random
while True:
    numero = int(random.randint(1, 10)) # generamos numero aleatorio entre el 1 y el 10
    if numero ==  5:
        print('Numero correcto = {numero}')
        print('Estás dentro')
        break
    print(numero)