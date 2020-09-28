# esto es un sumatorio. si introduces un numero realiza lo siguiente:
# ejemplo 1 = 5 . 5+4+3+2+1 = 15
# ejemplo 2 = 7+6+5+4+3+2+1 = 28

def sumatorio(num):
	if num == 1:
		return 1 # solo devolvera 1 cuando la condicion se cumpla
	else:
		return num + sumatorio(num - 1) # aqui se llama a la funcion
		# siempre que la variable no sea 1 sumará num más el sumatorio de n-1 y así recursivamente.

num = int(input("Número para realizar el sumatorio = "))
print(sumatorio(num))