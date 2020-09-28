import math # importamos la libreria math que necesitaremos para calcular la raiz cuadrada
# creamos la clase
class Triangulo:

    # declaramos el metodo __init__ para inicializar los atributos que pedimos por input
    def __init__(self):
        self.lado_A = float(input('Pon el valor del lado A del triángulo en centímetros: '))
        self.lado_B = float(input('Pon el valor del lado B del triángulo en centímetros: '))
        self.lado_C = float(input('Pon el valor del lado C del triángulo en centímetros: '))

    # método para imprimir los lados
    def imprimir(self):
        """Método propio de la clase triangulo para imprimir los lados del triángulo."""
        print(f"Lado A del triángulo: {self.lado_A} centímetros.")
        print(f"Lado B del triángulo: {self.lado_B} centímetros.")
        print(f"Lado C del triángulo: {self.lado_C} centímetros.")

    # método para averiguar si el triángulo es equilátero, isósceles o escaleno
    def tipo_triangulo(self):
        """Método propio de la clase triangulo para averiguar si el triángulo es equilátero, isósceles o escaleno."""
        # si todos los lados son iguales es equilátero
        if self.lado_A == self.lado_B and self.lado_B == self.lado_C: 
            return "Equilátero"
        # si el triángulo solo tiene dos lados iguales es isósceles
        elif (self.lado_A == self.lado_B and self.lado_B != self.lado_C) or (self.lado_A != self.lado_B and self.lado_B == self.lado_C) or (self.lado_A == self.lado_C and self.lado_B != self.lado_C):
            return "Isósceles"
        # si los tras lados son desiguales es escaleno
        else:
            return "Escaleno"

    # método para calcular área del triángulo usando la formula de Herón
    def calcular_area_triangulo(self):
        """Método propio de la clase triangulo para calcular el área del triángulo usando la formula de Herón."""
        # primero hay que calcular el semiperímetro
        s = 0.0 # iniciamos variable semiperimetro
        s = (self.lado_A + self.lado_B + self.lado_C)/2
        # y luego aplicar la formula de Herón. Raiz cuadrada de (s*((s-a)*(s-b)*(s-c)))
        area = math.sqrt((s*((s-self.lado_A)*(s-self.lado_B)*(s-self.lado_C))))
        return area

# instanciamos la clase creando un objeto
triangulo1 = Triangulo()
# probamos sus metodos
triangulo1.imprimir()
print(f"El tipo de triángulo es = {triangulo1.tipo_triangulo()} .")
print(f"El área del triángulo es = {triangulo1.calcular_area_triangulo()} centímetros cuadrados.")


