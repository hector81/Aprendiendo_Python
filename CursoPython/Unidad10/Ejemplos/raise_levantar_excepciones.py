def probable_execp(numero):
    """Función que sintácticamente está perfecta
        pero no lógicamente
    """
    numero = float(numero)
    raiz = numero ** 0.5
    if numero <0:
        raise Exception("El dato introducido debe ser un número positivo")
    else:
        print(f"La raíz cuadrada del número {numero} es {raiz}")
    print("Buen día.")


numero = input("Introduce número: ")
probable_execp(numero)