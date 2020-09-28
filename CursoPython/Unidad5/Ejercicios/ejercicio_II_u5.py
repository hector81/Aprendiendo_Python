'''
Escribe un programa que resuelva el siguiente problema.
Lea la cantidad de Kw que ha consumido una familia teniendo en cuenta que el precio por Kw 0.135€. 
Si la cantidad es mayor a 700, incremente el precio en 5% para el exceso de Kw sobre 700. 
Muestre el valor total a pagar.
Recuerda:
Gasto = Consumo * precio
Gasto_extra = consumo_extra *(precio + precio* 5%)
Total_a_pagar=Gasto + Gasto_extra
'''

consumo = float(input("¿Qué cantidad de kw ha consumido la familia Pérez?: "))
precio = 0.135
if consumo < 701:
    gasto = consumo * precio
    total_a_pagar = gasto
else:
    gasto = consumo * precio
    consumo_extra = consumo - 700
    gasto_extra = consumo_extra *(precio + precio * (5/100))
    total_a_pagar = gasto + gasto_extra

print(f"El total a pagar es: {total_a_pagar}")