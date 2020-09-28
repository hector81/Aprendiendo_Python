def excepcion_basica(numero):

    ocurre_error = False
    try:
        if numero <0:
            raise ValueError ("El dato introducido debe ser un número positivo")
 
    except TypeError:
        ocurre_error = True
        print("Ocurrió un error previsto.")
    except ValueError as descripcion:
        ocurre_error = True
        print("Ocurrió un error previsto. Tipo valor erroneo", descripcion)
    except:
        ocurre_error = True
        print("¡No sé qué pasó!")
    else:
        numero = float(numero) 
        calculo = numero ** 0.5 
        print(f"La raíz cuadrada del número {numero} es {calculo}")
        print("Buen día.")

excepcion_basica("6j")
excepcion_basica(-90)
excepcion_basica(87)
#excepcion_basica(hola)