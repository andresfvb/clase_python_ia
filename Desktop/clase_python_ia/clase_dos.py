# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:26:14 2021

@author: Andres Vasquez
"""

# Condicionales

x = 2
if(x > 0):
    print('1')
else:
    print('2')
    print('3')

# Algoritmo que dada la eda diga si es mayor o menor de endad

edad = int(input('Digite la edad de la persona: '))
if(edad >= 18):
    print("La persona es mayor de edad")
else:
    print("La persona es menor de edad")

# Coloque una nota y diga si aprobo o no

nota = float(input('Digite la nota del estudiante '))
if(nota >= 3 and nota <= 5):
    print("El estudiante aprobo")
elif(nota < 3):
    print("Usted perdio la materia")
else:
    print("El valor no es valido")

# Decir si el numero dado es positivo, negativo o es 0

numero = float(input('Digite el numero a verificar '))
if(numero > 0):
    print("El numero es positivo")
elif(numero < 0):
    print("El numero es negativo")
else:
    print("El numero es 0")
