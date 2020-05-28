'''
6. Cree un programa Python llamado . Cuando ejecute la instrucción en la consola de windows
donde numero1 y numero2 son dos números cualesquiera (enteros o decimales).
*******  python operaciones.py numero1 numero2 ************
Deberá mostrar por pantalla el resultado de la suma, resta, multiplicación y
división (si esta última es posible) de numero1 y numero2.
'''
import sys
import Ejercicio1_operaciones_basicas
python Ejercicio1_operaciones_basicas.py numero1 numero2
if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('ERROR: Necesitamos 2 parametros.')
	else:
		num1 = float(sys.argv [1])
		num2 = float(sys.argv [2])
		print('suma =' + str(Ejercicio1_operaciones_basicas.sumar (num1, num2)))
		print('resta ='+ str(Ejercicio1_operaciones_basicas.restar (num1, num2)))
		print('multiplicacion ='+ str(Ejercicio1_operaciones_basicas.multiplicar (num1, num2)))
		# la operacion division es peligrosa. Tenemos que controlar la excepcion
		try:
			print('division =' +  str(Ejercicio1_operaciones_basicas.dividir (num1, num2)))
		except ValueError:
			print('Division: Operacion no valida.')
