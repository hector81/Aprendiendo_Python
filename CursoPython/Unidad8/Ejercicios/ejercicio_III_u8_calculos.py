# importamos funciones que necesitamos del modulo ejercicio_III_u8_areas y les ponemos alias
from ejercicio_III_u8_areas import calcular_area_rectangulo as rectangulo, calcular_area_triangulo as triangulo, calcular_area_circulo as circulo

if __name__ == "__main__":
    print('Ejecutando como programa principal')
    print("Calcula el área de un rectángulo de 5 x 9.")
    print(rectangulo(5, 9))
    print("Calcula el área de un triangulo de 5 x 13.")
    print(triangulo(5, 13))
    print("Calcula el área de un criculo de 5 de radio.")
    print(circulo(5))


