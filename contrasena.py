# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 04:43:39 2024

@author: PC
Practica 03: Generador de contraseñas
Crear un sistema que genere una contraseña aleatoria

Para solucionar este problema se requiere listas, listas mayúsculas,
 lista de minúsculas, lista de números y lista de símbolos y luego armar una 
 contraseña aleatoria sacando caracteres de estas listas.
"""
# GENERADOR DE CONTRASEÑAS
"""import random
import string

letras_mayusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = string.punctuation
caracteres = letras_mayusculas + letras_minusculas + numeros + simbolos + caracteres

print(letras_mayusculas)
print(letras_minusculas)
print(numeros)
print(simbolos)
print(caracteres)"""


import random
import string

def generar_contraseña(longitud):
    # Definir listas de caracteres
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Combinar todas las listas en una sola lista de caracteres
    caracteres = letras_mayusculas + letras_minusculas + numeros + simbolos

    # Generar contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))

    print(contraseña)


generar_contraseña(5)



