# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 04:11:25 2024

@author: PC

Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa 
y muestre su símbolo o un mensaje de aviso si la divisa no está en el 
diccionario
"""

monedas = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
get_moneda = input("Especifique tipo de moneda: ")
get_moneda = get_moneda.capitalize()
encontrado = False


for coin in monedas:
    if get_moneda == coin:
        simbolo = monedas[coin]
        encontrado = True
        print(f"El simbolo de {coin} es {monedas[coin]}")

if encontrado == False:
    print("la divisa no está en el diccionario")






