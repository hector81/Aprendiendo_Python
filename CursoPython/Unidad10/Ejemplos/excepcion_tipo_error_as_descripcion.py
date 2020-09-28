def excepcion_basica(numero):
    descripcion = "problematico"
    ocurre_error = False
    try:
        numero = float(numero)
        calculo = numero ** 0.5
        print(f"La raíz cuadrada del número {numero} es {calculo}")
 
    except TypeError as descripcion:
        ocurre_error = True
        print("Ocurrió un error previsto:  ", descripcion)
    except:
        ocurre_error = True
        print("¡No sé qué pasó!")
    if ocurre_error:
        print("Lástima.")
    else:
        print("Buen día.")

'''
Prueba en tu espacio de trabajo, excepcion_basica("6j"), 
excepcion_basica(-90), excepcion_basica(87), excepcion_basica(hola)
'''
excepcion_basica("6j")
excepcion_basica(-90)
excepcion_basica(87)
#excepcion_basica(hola)