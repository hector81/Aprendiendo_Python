def excepcion_basica(numero):
 
    control_error = False
    try:
        numero = float(numero)
        calculo = numero ** 0.5
        print(f"La raíz cuadrada del número {numero} es {calculo}")
    except:
        control_error = True
    if control_error:
        print("lástima hubo una excepción")
    else:
        print("Buen día.")

'''
Prueba en tu espacio de trabajo, excepcion_basica("6j"), 
excepcion_basica(-90), excepcion_basica(87), excepcion_basica(hola)
'''
#excepcion_basica("6j")
#excepcion_basica(-90)
#excepcion_basica(87)
#excepcion_basica(hola)