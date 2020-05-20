'''
EJERCICIOS EXCEPCIONES
1. Función que recibe dos enteros, a y b, y divide el mayor por el menor mostrando
un mensaje de error si es una división entre cero (ZeroDivisionError).
'''
def introducirNumero():
     while True:
         try:
             x = int(input("Por favor ingrese un número: "))
             return x
             break
         except ValueError:
             print("Oops! No era válido. Intente nuevamente...")

def dividir(a, b):
    lista = [a, b]
    maximo = max(lista)
    minimo = min(lista)
    try:
        resultado = maximo / minimo
        return f"El resultado de la division ({maximo}/{minimo}) es = {resultado}"
    except ZeroDivisionError:
        return f"El denominador o divisor no puede ser cero"

print(f"Introduce el parametro a")
a = introducirNumero()
print(f"Introduce el parametro b")
b = introducirNumero()
print(dividir(a, b))
