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
print('Hola',nombre)

print('Digite su nombre: ')
nombre = input()
print('Hola',nombre)

# SUMA DOS NUMERO E IMPRIMA RESULTADO

n1 = float(input ('digita el primer numero: '))
n2 = float(input ('digita el segundo numero: '))
nr = n1 + n2
print('La suma de',n1,'+',n2,'es',nr)