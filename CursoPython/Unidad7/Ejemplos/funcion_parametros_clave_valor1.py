# funcion con parametro predefinido

def saludo(nombre, apellidos, trato = 'Sra'):
    print('Hola ', trato, ' ',nombre, ' ', apellidos)

#no hace falta seguir el orden de los parametros de la funcion mientras estén las variables
saludo(nombre = 'Juana', apellidos= 'García',)

'''
ESTO DARIA ERROR PORQUE NO SIGUE EL ORDEN DE LOS PARAMETROS
def saludo( trato = 'Sra', nombre, apellidos):
    print('Hola ', trato, ' ',nombre, ' ', apellidos)

#no hace falta seguir el orden de los parametros de la funcion mientras estén las variables
saludo(nombre = 'Juana', apellidos= 'García',)
'''