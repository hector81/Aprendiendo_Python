def introducirVariable():
     while True:
         try:
             x = input("Por favor ingrese la palabra: ")
             if x != '':
                 return x
                 break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def comprobarExisteUsuario(arrayUsuariosClave,nombre):
    nombre = nombre.upper()
    posicion = ''
    boolComp = False
    for i in range(len(arrayUsuariosClave)):
        posicion = arrayUsuariosClave[i][0].upper()
        if posicion == nombre:
            boolComp = True
    return boolComp

def comprobarExisteUsuarioClave(arrayUsuariosClave,nombre,clave):
    nombre = nombre.upper()
    posicion = ''
    boolComp = False
    for i in range(len(arrayUsuariosClave)):
        posicion = arrayUsuariosClave[i][0].upper()
        if posicion == nombre:
            if clave == arrayUsuariosClave[i][1]:
                boolComp = True
    return boolComp

def respuestaCorrecta():
    while True:
        try:
            x = int(input('¿Quieres probar otra vez (1-Si/2-No)? '))
            if x == 1 or x == 2:
                return x
                break
            else:
                print("La respuesta solo puede ser 1 o 2")
        except ValueError:
            print("La respuesta solo puede ser 1 o 2")


arrayUsuariosClave = [
    ['pepe44','alfa'],
    ['sara33','bravo'],
    ['javi','zulu']
]

respuesta = 1

while respuesta == 1:
    print("introduzca usuario")
    usuario = introducirVariable()
    if comprobarExisteUsuario(arrayUsuariosClave,usuario) == True:
        print("Usuario correcto, introduzca clave")
        clave = introducirVariable()
        if comprobarExisteUsuarioClave(arrayUsuariosClave,usuario,clave) == True:
            print("USUARIO Y CLAVE CORRECTOS")
        else:
            print("El usuario es correcto pero la clave no coincide")
    else:
        print("El usuario no está en la base de datos")

    respuesta = respuestaCorrecta()
