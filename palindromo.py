# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 04:44:52 2024

@author: PC

Practica 01: Palíndromo
Crear un sistema que detecte si una palabra es palíndroma o no

Para solucionar este problema el usuario tiene que ingresar por pantalla una palabra y el sistema verificas si es palíndromo o no.

Una palabra palíndroma se lee de igual formo como de la derecha y de la izquierda.
"""
# PALINDROMO

import re


def palindromo():
    # Recolectar datos 
    palabra = input("Por favor ingrese la palabra: ")
    
    # Limpiar la cadena y quitar acentos
    palabra_limpia = (re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚ]', '', palabra.lower()))
    
    # Reversar la cadena
    palabra_reverse = palabra_limpia[::-1]
    
    # Comparar ambas cadenas e imprimir resultados
    if palabra_limpia == palabra_reverse:
        print(f"La palabra o frase: {palabra} es un Palíndromo")
    else:
        print(f"La palabra o frase: {palabra} no es un Palíndromo")

palindromo()





