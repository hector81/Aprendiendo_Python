'''
El precio de un kebab depende de su tamaño según la siguiente tabla
nombre variable	  Precio   valor variable
pequeño		  3€       1
mediano           5€       2
grande            9€       3

Cada ingrediente extra incrementa 0.5€ el precio del kebab
'''
tamano = int(input("Tamaño del kebab: "))
n = int(input("Número de ingredientes extra: "))

# el pequeño es 3, el mediano  es 2 y el 1 es grande

if tamano ==1:
	pagar = 3 + (0.5*n)
elif tamano == 2:
	pagar = 5 + (0.5*n)
elif tamano == 3:
	pagar = 9 + (0.5*n)
else:
	pagar = 0 # 'No seleccionaste nada'
print(f'Debes pagar {pagar}€')