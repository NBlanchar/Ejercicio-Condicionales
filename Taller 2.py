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
    else:
        total = total_compra - (total_compra * 0.15)
    print(f'El total a pagar es: ${total:,}')
else:
    print("Digite un valor a pagar valido")

# Ejercico 3
fianza = float(input('Digite el valor de la fianza: '))
if(fianza > 0):
    if(fianza < 50000):
        cuota = fianza * 0.03
    else:
        cuota = fianza * 0.02
    print(f'El valor de la cuota a pagar es: ${cuota:,}')
else:
    print("Digite un valor a pagar valido")

# Ejercicio 4
produccion = int(input('Digite el total de dias de producción: '))
if (produccion >= 14):
    puntos = int(input('Digite la cantidad de puntos de control ambiental: '))
    ganancias = float(input('Digite el valor de las ganancias diarias: '))
    acumulador = 0
    for x in range(puntos):
        D_uno = int(input(f'Emision del punto {x+1} el primer dia: '))
        D_dos = int(input(f'Emision del punto {x+1} el segundo dia: '))
        D_tres = int(input(f'Emision del punto {x+1} el tercer dia: '))
        D_cuatro = int(input(f'Emision del punto {x+1} el cuarto dia: '))
        D_cinco = int(input(f'Emision del punto {x+1} el quinto dia: '))
        acumulador = acumulador + D_cinco + D_cuatro + D_tres + D_dos + D_uno
    promedio = acumulador / (puntos * 5)
    if(promedio > 170):
        perdida = (7 * ganancias) + ((produccion - 7) * ganancias * 0.5)
    else:
        perdida = 0
    print(f'las perdidas generadas por la inspección es: ${perdida:,}')
else:
    print('La producción debe duarar minimo 14 dias')

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
        costo = costo - (costo * 0.1)
    costo = costo + (costo * 0.16)
    print(f'EL total a pagar por el equipo es: ${costo:,}')
else:
    print("Digite valor valido")

# Ejercicio 8
precio = float(input('Digite el monto de la compra: '))
prestamo = 0
if(precio > 0):
    if(precio > 500000):
        inversion = precio * 0.55
        prestamo = precio * 0.30
        credito = precio * 0.15
    else:
        inversion = precio * 0.7
        credito = precio * 0.3
    interes = credito * 0.20
    print(f'El valor de la inversión es: ${inversion:,}')
    print(f'El valor del prestamos bancario es: $ {prestamo:,}')
    print(f'EL valor del credito al fabricante es: ${credito:,}')
    print(f'El valor del interes al fabricante es: ${interes:,}')
else:
    print('Digite un valor valido')

# Ejercicio 9
num1 = float(input('Digite numero 1: '))
num2 = float(input('Digite numero 2: '))
if(num1 == num2):
    resultado = num1 * num2
elif(num1 > num2):
    resultado = num1 - num2
else:
    resultado = num1 + num2
print(f'El resultado de la operación es: {resultado}')

# Ejercicio 10
num1 = float(input('Digite numero 1: '))
num2 = float(input('Digite numero 2: '))
num3 = float(input('Digite numero 3: '))
if(num1 != num2 and num1 != num3 and num2 != num3):
    if(num1 > num2 and num1 > num3):
        print(f'El numero mayor es {num1}')
    elif(num2 > num1 and num2 > num3):
        print(f'El numero mayor es {num2}')
    else:
        print(f'El numero mayor es {num3}')
else:
    print('Los numero deben ser diferentes')
    