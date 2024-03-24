# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 04:37:47 2024

@author: PC
Escribir un programa que pregunte al usuario su nombre, edad, dirección y
 teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla
 el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de 
 teléfono es <teléfono>.
"""

datos = ("nombre", "edad", "direccion", "telefono")

datos_recibidos = {}

for dato in datos:
    valor = input(f"Ingrese su {dato}: ")
    datos_recibidos[dato] = valor
    

print(datos_recibidos)
print(datos_recibidos["nombre"], " tiene ", datos_recibidos["edad"], " años, vive en ", datos_recibidos["direccion"], " y su número de teléfono es ", datos_recibidos["telefono"])
