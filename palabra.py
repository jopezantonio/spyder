# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 04:02:57 2024

@author: PC
Escribir un programa que pida al usuario una palabra y luego muestre por 
pantalla una a una las letras de la palabra introducida empezando por la 
última.
"""

word = input("Por favor introduzca una palabra: ")
word = word[::-1]
i = 0

while i < len(word):
    print(word[i])
    i +=1