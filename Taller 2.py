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

# Ejercico 3
fianza = float(input('Digite el valor de la fianza: $'))
if(fianza > 0):
    if(fianza < 50000):
        cuota = fianza * 0.03
    else:
        cuota = fianza * 0.02
    print(f'El valor de la cuota a pagar es: ${cuota:,}')
else:
    print("Digite un valor a pagar valido")

# Ejercicio 4

# Ejercicio 5
devaluacion = float(input('Porcentaje de devalucación del vehiculo: '))
valorizacion = float(input('Porcentaje de valorización del terreno: '))
if(devaluacion * 3 <= valorizacion * 1.5):
    print('Se recomienda comprar el vehiculo')
else:
    print('Se recomienda comprar el terreno')

# Ejercicio 6
num_computadores = int(input('Digite la cantidad de computadores a comprar: '))
subtotal = 11000 * num_computadores
if(num_computadores > 0):
    if(num_computadores < 5):
        total = subtotal - (subtotal * 0.1)
    elif(num_computadores >= 5 and num_computadores < 10):
        total = subtotal - (subtotal * 0.2)
    else:
        total = subtotal - (subtotal * 0.4)
    print(f'El total sin descuento es: ${subtotal}')
    print(f'El total a pagar es: ${total}')
else:
    print('Digite un valor valido')

# Ejercicio 7
costo = float(input('Digitar costo del equipo sin iva: '))
marca = input('Digitar marca del equipo: ')
if(costo > 0):
    if(costo >= 2000 and marca == 'NOSY'):
        costo = costo - (costo * 0.15)
    elif (marca == 'NOSY'):
        costo = costo - (costo * 0.05)
    elif(costo >= 2000):
        costo = costo - (costo * 0.05)
    costo = costo + (costo * 0.16)
    print(f'EL total a pagar por el equipo es: ${costo}')
else:
    print("Digite valor valido")
        