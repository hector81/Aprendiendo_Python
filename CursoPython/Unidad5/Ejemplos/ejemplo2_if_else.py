total_compra = float(input('Gasto de compra = '))
importe_a_pagar = total_compra

if total_compra > 100:
    tasa_descuento = 15
    importe_descuento = total_compra * tasa_descuento/100
    importe_a_pagar = total_compra - importe_descuento
    print(f"Como has sobrepasado el gasto común recibes un descuento del 15%, así que de {total_compra}, has pagado {importe_a_pagar}")
else:
    print(f"Has pagado {importe_a_pagar}")
    diferencia = 100 - total_compra
    print(f'Si gastases {diferencia}€ más, recibirías el 15 % de descuento')