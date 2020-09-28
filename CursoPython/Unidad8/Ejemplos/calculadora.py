# costruccion de un modulo
def suma(a,b):
    """ Función que realiza la suma de a + b """
    print("el resultado de la suma es: ",a+b)
 
def resta(a,b):
    """ Función que realiza la resta de a - b """
    print("el resultado de la resta es: ",a-b)
 
def multiplica(a,b):
    """ Función que realiza la multiplicación de a * b """
    print("el resultado de la multiplicación es: ",a*b)
 
def divide(a,b):
    """ Función que realiza la división de a * b """
    print("el resultado de la división es: ",a/b)

# si se cumple esta condición se ejecutará el programa principal
if __name__ == "__main__":
    print("Estoy ejecutando el programa principal")
    #ESTE DA ERROR POR POR LA IDENTATION---suma(6,5)# ejemplo de sentencia que se ejecutará en caso de ejecutarse como un programa
# Si no se ha importado (se ha ejecutado como programa principal) ejecuta el código dentro del condicional.
#suma(6,5)# ejemplo de sentencia que se ejecutará en caso de ejecutarse como un programa

#si no se cumple, lo hemos llamado de otro lugar y esta ejecucion no se llevaria a cabo y 
# se ejecutarian las operaciones del programa principal
'''
__main__ es el nombre del ámbito en el que se ejecuta el código de nivel superior en el programa principal.
'''