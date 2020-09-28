def probable_execp(numero):
    """Función que sintácticamente está perfecta
        pero no lógicamente
    """
 
    if type(numero) is str:
        raise Exception("El dato introducido debe ser un número")
    elif numero <0:
        raise Exception ("El dato introducido debe ser un número positivo")
    else:
        numero = float(numero)
        calculo = numero ** 0.5
        print(f"La raíz cuadrada del número {numero} es {calculo}")
    print("Buen día.")


numero = input("Introduce número: ")
probable_execp(numero)