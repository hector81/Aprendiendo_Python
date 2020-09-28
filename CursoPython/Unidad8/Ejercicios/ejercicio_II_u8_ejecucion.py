from paquete.ejercicio__II_u8_modulo  import ingresar_cantidad_compra as ingresar, comprobar_cantidad as comprobar, seleccionar_bola_descuento as bola, aplicar_descuento as descontar

if __name__ == "__main__":
    cantidad = ingresar() # ingresamos cantidad
    if comprobar(cantidad) == False: # comprbamos que la cantidad sea menor o mayor o igual que 100 euros
        print(f"La cantidad es menor de 100 euros y no se aplica ningún descuento. La cantidad a pagar es {cantidad} euros.")
    else:
        print(f"La cantidad {cantidad} es mayor o igual que 100 euros y se te puede aplicar algún descuento dependiendo de la bola que te toque.")
        descuento = bola() # seleccionamos bola aleatoria con descuento
        descontar(cantidad, descuento) # imprimimos el precio con descuento