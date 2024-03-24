# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 06:47:21 2024

@author: PC
"""




def convertir():
    denominaciones = {
    "bolivares" : 36.28,
    "soles" : 3.70,
    "reales" : 4.97,
    "euros" : 0.92,
    "pesos_arg" : 850.32}

    print("PROGRAMA CONVERSOR DE MONEDAS A DOLARES")
    print("\n")
    menu = """ 
    1. Bolivares a Dolares
    2. Soles a Dolares
    3. Reales a Dolares
    4. Euros a Dolares
    5. Pesos Argentinos a Dolares

    Ingrese una opcion: """
    opcion = input(menu)
    if opcion == "1":
        moneda = denominaciones["bolivares"]
        divisa = "bolivares"
    elif opcion == "2":
        moneda = denominaciones["soles"]
        divisa = "soles"
    elif opcion == "3":
        moneda = denominaciones["reales"]
        divisa = "reales"
    elif opcion == "4":
        moneda = denominaciones["euros"]
        divisa = "euros"
    elif opcion == "5":
        moneda = denominaciones["pesos_arg"]
        divisa = "pesos argentinos"
    cantidad = float(input(f"Ingrese la cantidad de {divisa}: "))
    resultado = cantidad / moneda
    
    print(f"La cantidad en dolares es: {round(resultado, 2)}")

    
convertir()




