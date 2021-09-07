# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:50:16 2021

@author: Andres Vasquez
"""

print ('Hello World')

#Variables en Paython

a = 3
print(type(a))
a = "Hola"
print(type(a))
a = 3
y = str(a)
print(y)
print(type(y))

# capturar por pantalla

nombre = input('Digite su nombre: ')
print('Hola', nombre)

print('Digite su nombre: ')
nombre = input()
print('Hola', nombre)

# SUMA DOS NUMERO E IMPRIMA RESULTADO

n1 = float(input('digita el primer numero: '))
n2 = float(input('digita el segundo numero: '))
nr = n1 + n2

# print('La suma de',n1,'+',n2,'es',nr)

print('La suma de los numeros {n1} + {n2} es {suma}')

# Haga un numero y eleve al cuadrado

numero_uno = float(input('Digita el numero a elevar: '))
numero_resultante = pow(numero_uno, 2)
print(f'La potencia de {numero_uno} es {numero_resultante}')

# HAGA QUE TOME EL VALOR DE UN PRODUCTO Y APLIQUE EL 20%

numero_uno = float(input('Digita el valor del producto: $'))
descuento = numero_uno * 0.20
numero_resultante = numero_uno - descuento
print(f'Valor: ${numero_uno:,}')
print(f'Descuento del 20%: ${descuento:,}')
print(f'Valor final: ${numero_resultante:,}')

