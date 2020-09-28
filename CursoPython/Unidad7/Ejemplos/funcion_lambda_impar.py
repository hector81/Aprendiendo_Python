def impar1 (num) :
    """Función que comprueba si un número dado es impar
    """
    if num % 2 != 0:
        return True
    else:
        return False
print(impar1(5))


#Expresión lambda para realizar la solución al mismo problema
impar2 = lambda num: num%2 != 0
print(impar2(6))


