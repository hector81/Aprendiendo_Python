def probable_execp(numero):
    """Función que sintácticamente está perfecta
        pero no lógicamente
    """
    numero = float(numero)
    raiz = numero ** 0.5
    print(f"La raíz cuadrada del número {numero} es {raiz}")

''' Llamada sin errores  '''
#Como puedes comprobar si introducimos un número entero o float la función se ejecutará sin
#  problemas y no producirá errores.
probable_execp(9)
#La raíz cuadrada del número 9.0 es 3.0

''' Llamada con errores  '''
#Variable no definida
#   probable_execp(Hola) # NameError: name 'Hola' is not defined
#Variable mal definida
#   probable_excep('3,8') # ValueError: could not convert string to float: '3,8'
#Más valores de los esperados
#   probable_excep(3,8)  # TypeError: probable_execp() takes 1 positional argument but 2 were given