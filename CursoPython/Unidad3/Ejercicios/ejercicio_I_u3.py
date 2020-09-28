'''
Vas a crear un conversor de distancias, vas a escribir un programa que 
pida una medida en pulgadas y que escriba esa misma en centímetros.
Ten en cuenta que 1 pulgada =  2.56 centimetros
'''
distancia_pulgadas = float(input('Pon una distancia en pulgadas: '))
distancia_centrimetros = distancia_pulgadas * 2.56
print(f'La distancia en pulgadas es : {distancia_pulgadas} pulgadas.')
print(f'La distancia en centímetros es : {distancia_centrimetros} centímetros.')