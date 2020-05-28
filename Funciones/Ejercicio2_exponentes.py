'''
2. Función que recibe tres parámetros (x, y, z) y devuelve //// x ** y ** z """
 ParseError: KaTeX parse error: Expected '}', got 'EOF' at end of input: x^{y^z.
'''
def resultado_exponentes(x, y, z):
    resultado = (x ** y) ** z
    return resultado
def introducirNumero():
     while True:
         try:
             x = int(input(f"Por favor ingrese un número: "))
             if x > 0:
                 return x
                 break
             else:
                 print(f"El número debe ser mayor que 0")
         except ValueError:
             print(f"Oops! No era válido. Intente nuevamente...")

exponenteX = introducirNumero()
exponenteY = introducirNumero()
exponenteZ = introducirNumero()

print(f'Los exponentes (x,y,z) son ({exponenteX},{exponenteY},{exponenteZ})')
print(f'El resultado de los exponentes es = {resultado_exponentes(exponenteX, exponenteY, exponenteZ)}')
