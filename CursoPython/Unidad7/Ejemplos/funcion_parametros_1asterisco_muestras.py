# esto significaria que no sabe cuantas muestras va a haber pero que acepta un numero indefinido
# Estos argumentos se recibirán por la función como si fuera una tupla de valores.
# Parámetros múltiples indefinidos

def promedio(*muestras):
    """ Calcula el promedio de los valores que introduzcas"""
    promedio = sum(muestras)/len(muestras)
    print(f"El promedio es : {promedio}")

#llamada a la funcion
promedio(3,5,8,5,9,32)
#print(promedio._doc__)
#print(help(promedio))
