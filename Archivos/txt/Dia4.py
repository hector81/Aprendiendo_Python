import sys
# import cases

fichero = "License.txt"
fichero_camel_case = "LicenseCamelCase.txt"
fichero_snake_case = "license_snake_case.txt"
fichero_lower_case = "License_lower_case.txt"
fichero_upper_case = "license_upper_case.txt"

def to_camel_case(linea):
	return ''.join([p.capitalize() for p in linea.split()])

def to_snake_case(linea):
	return '_'.join([p.lower() for p in linea.split()])

def to_lower_case(linea):
	return linea.lower()

def to_upper_case(linea):
	return linea.upper()

PROCESADORES = [(fichero_camel_case,to_camel_case),
		(fichero_snake_case,to_snake_case),
		(fichero_lower_case,to_lower_case),
		(fichero_upper_case,to_upper_case)]

#PROCESO

fichero = sys.argv[1]
print(f'Vamos a procesar el fichero{fichero1}')
with open(fichero,'r') as f:
   datos = f.readlines()

for fichero1, funcion_proceso in PROCESADORES:
	with open(fichero1,'w') as f_out:
		for linea in datos:
			f_out.write(funcion_proceso(linea))
