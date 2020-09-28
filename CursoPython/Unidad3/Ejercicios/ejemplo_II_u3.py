'''
Programa que pida el largo y el ancho de un rectángulo y calcule su perímetro y su área.
Nota: el área de un rectángulo es base*altura y su perímetro 2*base + *altura
'''
print('Calcular el área y el perímetro de un rectángulo conociendo sus lados')
base = float(input('Introduce el valor de la base: '))
altura = float(input('Introduce el valor de la altura: '))
area = (base * altura) / 2
perimetro = 2*base / 2*altura
print(f'El área del rectángulo con una base {base} y una altura {altura} es : {area} ')
print(f'El perímetro del rectángulo con una base {base} y una altura {altura} es : {perimetro} ')