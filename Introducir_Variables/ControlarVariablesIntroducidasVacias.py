def lee_entero():
    bool = True
    while bool == True:
        entrada = input("Escribe un numero entero: ")
    try:
        entrada = int(entrada)
        print(entrada)
        bool = False
    except ValueError:
        print ("La entrada es incorrecta: escribe un numero entero")

lee_entero()
