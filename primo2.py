# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 00:23:41 2024

@author: PC
"""

num = int(input("Ingrese el numero: "))
i = 2
mitad =  num // 2
primo = True

while i <= mitad:
    if num % i == 0:
        primo = False
        break
    else: 
        i += 1
if primo:
    print(f"El numero {num} es primo.")
else:
    print(f"El numero {num} no es primo.")

