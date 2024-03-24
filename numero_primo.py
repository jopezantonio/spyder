# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 04:38:02 2024

@author: PC
Algoritmo de verificación: Para verificar si un número es primo, puedes seguir los siguientes pasos:

Comenzar con el número que quieres verificar.
Iterar sobre todos los números desde 2 hasta la mitad del número (o incluso hasta su raíz cuadrada).
En cada iteración, verifica si el número dado es divisible por el número actual del ciclo.
Si encuentra algún divisor, el número no es primo. De lo contrario, el número es primo.
"""

num = int(input("Ingrese un numero entero: "))
mitad = num // 2
i = 2
primo = True

while i <= mitad:
    if num % i == 0:
        primo = False
        break
    i += 1

if primo:
    print(f"El número {num} es primo.")
else:
    print(f"El número {num} no es primo.")
