# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:30:53 2021

@author: nefer
"""
import random

# Ejercicio 1
num_camisas = int(input('Digite el numero de camisas a comprar: '))
acumulador = 0
for x in range(num_camisas):
    camisa = float(input(f'Digite el precio de la {x+1} camisa: '))
    acumulador = acumulador + camisa
if(num_camisas > 0):
    print(f'El total sin descuento es: ${acumulador:,}')
    if(num_camisas >= 3):
        total = acumulador - (acumulador * 0.3)
        print(f'El total a pagar es: ${total:,}')
    else:
        total = acumulador - (acumulador * 0.1)
        print(f'El total a pagar es: ${total:,}')
else:
    print('Por lo menos debe comprar una camiseta')

# Ejercicio 2
total_compra = float(input('Digite el total de la compra: '))
num = random.randint(0, 100)
print(f'el numero al azar es: {num}')
if(total_compra > 0):
    if(num >= 74):
        total = total_compra - (total_compra * 0.2)
        print(f'El total a pagar es: ${total:,}')
    else:
        total = total_compra - (total_compra * 0.15)
        print(f'El total a pagar es: ${total:,}')
else:
    print("Digite un valor a pagar valido")
