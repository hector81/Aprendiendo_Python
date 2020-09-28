'''
Crear algoritmo, a través de pseudocódigo y después un programa que pida al usuario una
 cantidad de euros, una tasa de interés y un número de años y que como resultado muestre 
 por pantalla el resultado de cuánto se habrá convertido el capital inicial transcurridos 
 esos años si cada año se aplica la tasa de interés introducida.

Solo recuerda que un capital de  X  euros a un interés del  z  por cien durante n años se calcula: 
X· (1 + z/100)**n euros.
'''
capital = float(input('Pon el capital inicial que quieres en invertir en euros: '))
interes = float(input('Pon la tasa de interés anual: '))
years = int(input('Pon los años que quieres mantener el capital invertido: '))

print(f'El capital inicial será de  {capital} euros.')
print(f'La tasa de interés anual es {interes}%.')
print(f'Los años que vas a dejar el capital invertido son {years} años.')

resultado_final = capital * (1 + interes/100) ** years

print(f'El resultado final de tu inversión será de : {resultado_final} euros.')