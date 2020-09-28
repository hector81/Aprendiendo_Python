# importamos funciones que necesitamos del modulo ejercicio_I_u8_modulo y les ponemos alias
from ejercicio_I_u8_modulo import generar_7_numeros_aleatorios as generar, mostrar_lista as mostrar, ordenar_valores_lista as ordenar

if __name__ == "__main__":
    print('Ejecutando como programa principal')
    print("Generando la lista")
    lista = generar()
    print("Imprimiendo la lista")
    mostrar(lista)
    print("\nOrdenando la lista")
    ordenar(lista)
    print("Volviendo a imprimir la lista")
    mostrar(lista)
