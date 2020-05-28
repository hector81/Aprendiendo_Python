'''
1. Cree un módulo llamado operaciones_basicas.py con las siguientes funciones: sumar, restar, multiplicar, dividir.
 *Cada función recibirá dos parámetros (los operandos).
 *Cada función devolverá el resultado de la operación correspondiente.
 *Controle la excepción de la división por cero en la función dividir.
 *Documente el módulo y las funciones con las siguientes cadenas de texto:
    -• Modulo --> Módulo Operaciones_basicas.
    -• sumar --> Función que suma los dos parámetros y devuelve el resultado.
    -• restar --> Función que resta los dos parámetros y devuelve el resultado.
    -• multiplicar --> Función que multiplica los parámetros y devuelve el resultado.
    -• dividir --> Función que divide los parámetros (numerador, denominador) y devuelve el resultado. Captura
       la excepción que generaría una división por cero.
       El código de esa excepción mostrará el mensaje
       'ERROR: No se puede dividir por cero' y relanzará una excepción del tipo ZeroDivisionError
'''
# funciones
def sumar(operando1, operando2):
    resultado = operando1 + operando2
    return resultado

def restar(operando1, operando2):
    resultado = operando1 - operando2
    return resultado

def multiplicar(operando1, operando2):
    resultado = operando1 * operando2
    return resultado

def dividir(operando1, operando2):
    numerador = operando1   #dividendo
    denominador = operando2 #divisor
    try:
        resultado = numerador / denominador
        return resultado
    except ZeroDivisionError:
        print(f"El denominador o divisor no puede ser cero")
        return -1
