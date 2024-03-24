# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 04:34:28 2024

@author: PC
Escribir una función que reciba una muestra de números en una lista y devuelva 
su media.
"""

lista = []
sumatoria = 0

def media():
    for _ in range(4):
        num = int(input("Ingrese numeros para la lista: "))
        lista.append(num)
    print(lista)
    
    for n in lista:
        global sumatoria
        sumatoria += n
        
    return sumatoria / len(lista)

resultado = media()
print("La media de los numeros ingresados es: ", resultado)
