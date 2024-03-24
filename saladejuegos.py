# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 05:05:15 2024

@author: PC

Escribir un programa para una empresa que tiene salas de juegos
 para todas las edades y quiere calcular de forma automática el
 precio que debe cobrar a sus clientes por entrar. El programa 
 debe preguntar al usuario la edad del cliente y mostrar el 
 recio de la entrada. Si el cliente es menor de 4 años puede 
 entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si
 es mayor de 18 años, 10€.
"""

print("*" * 20, "Sala de Juegos", "*" * 20, "\n" * 2)
user_age = int(input("Por favor ingrese la edad del usuario: "),)
print("\n")

if user_age > 0 and user_age <= 120:
    if user_age < 4:
        print(f"El usuario de {user_age} años no paga")
        print("=" * 32)
    elif user_age >= 4 and user_age <= 18:
        print(f"El usuario de {user_age} años debe pagar 5$")
        print("=" * 32)
    else:
        print(f"El usuario de {user_age} debe pagar 10$")
        print("=" * 32)
else:
    print("Parametros de edad no permitidos")
