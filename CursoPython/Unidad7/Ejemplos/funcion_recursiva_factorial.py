def factorial (num):
    if num == 1:
        return 1 #solo devolverá 1 cuando la condición se cumpla
    else:
        return num * factorial(num - 1)#aquí se llama a la funcion para hacer la recursividad
             # siempre que la variable no sea 1 multiplicará num por el factorial de n-1 y así recursivamente.
 
num = int(input("Número para realizar el factorial: "))
print(factorial(num))