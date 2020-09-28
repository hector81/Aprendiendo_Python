# esto significaria que acepta un diccionario con clave valor como parametros
# Parámetros múltiples por clave-valor

def indeterminados_nombre1(**kwargs):
   print(kwargs)

indeterminados_nombre1(n=89, c="Hola Juan", l=[1,2,3,4,5])


def indeterminados_nombre2(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

indeterminados_nombre2(n=5, c="Hola Plone", l=[1,2,3,4,5])