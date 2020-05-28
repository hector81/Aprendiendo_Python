'''
7. Modifique el ejercicio anterior de la siguiente forma:
-Si el número de parámetros es 1, muestre el siguiente mensaje por pantalla 'ERROR: Necesito mas de un numero'.
-Si el número de parámetros es igual a dos, calcule la suma de ambos.
-Si se pasan 3 o más parámetros, realice las operaciones suma de forma asociativa y muestre su resultado.

Ejemplo:
            python operaciones.py 10 2 5
mostrará por pantalla
            suma = 17  # (10 + 2 + 5)
La operación división es un poco más compleja de programar si se gestionan las excepciones
 que puede producir. Si se siente con fuerzas, intente programar la división asociativa.

'''
import operaciones_basicas

if __name__ == '__main__':
	if len (sys.argv) == 2:
		print 'Necesito mas de un numero'
	elif len (sys.argv) == 3:
		num1 = float (sys.argv [1])
		num2 = float (sys.argv [2])
		print 'suma =', operaciones_basicas.sumar (num1, num2)
		print 'resta =', operaciones_basicas.restar (num1, num2)
		print 'multiplicacion =', operaciones_basicas.multiplicar (num1, num2)
		# la operacion division es peligrosa. Tenemos que controlar la excepcion
		try:
			print 'division =', operaciones_basicas.dividir (num1, num2)
		except ValueError:
			print 'Division: Operacion no valida.'
	elif len (sys.argv) > 3:
		num = [] #lista de numeros
		for p in sys.argv [1:]: # el primer valor de sys.argv es el nombre del programa
			num.append (float (p)) # transformo de cadenas de texto a float

		# suma asociativa
		suma = operaciones_basicas.sumar (num [0], num [1])
		for n in num [2:]:
			suma =  operaciones_basicas.sumar (suma, n)
		print 'suma =', suma

		# resta asociativa
		resta = operaciones_basicas.restar (num [0], num [1])
		for n in num [2:]:
			resta =  operaciones_basicas.restar (resta, n)
		print 'resta =', resta

		# multiplicacion asociativa
		multiplicacion = operaciones_basicas.multiplicar (num [0], num [1])
		for n in num [2:]:
			multiplicacion =  operaciones_basicas.multiplicar (multiplicacion, n)
		print 'multiplicacion =', multiplicacion

		# division asociativa
		error = False
		try:
			division = operaciones_basicas.dividir (num [0], num [1])
		except ValueError:
			print 'division = No se puede realizar'
			error = True
		for n in num [2:]:
			if error == True:
				break
			try:
				division =  operaciones_basicas.dividir (division, n)
			except ValueError:
				print 'division = No se puede realizar'
		if error == False:
			print 'division =', division
