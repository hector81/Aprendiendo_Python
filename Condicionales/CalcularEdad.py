edad = 0
# bucle para poner numero correto
while edad < 1:
    # ponemos el numero
    edad = int(input('Escribe tus años '))
    if edad < 1:
        print('El número debe ser positivo')

if edad < 18:
    print('Eres un menor')
elif edad > 17 or edad < 68:
    print('Eres un adulto')
else:
    print('Eres un anciano')
