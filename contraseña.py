# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 00:05:13 2024

@author: PC

Escribir un programa que almacene la cadena de caracteres contraseña en una 
variable, pregunte al usuario por la contraseña hasta que introduzca la 
contraseña correcta.
"""

contraseña = "naye3003"

while True:
    con_recibida = input("Por favor ingrese su contraseña: ")

    if con_recibida == contraseña:
        print("Su contraseña es correcta")
        break
    else:
        print("Su contraseña es incorrecta, por favor inténtelo de nuevo.")
