# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 05:28:50 2024

@author: PC
python
Copy code
mi_diccionario = {}  # Crear un diccionario vacío
mi_diccionario["clave"] = "valor"  # Agregar un elemento clave-valor
Método update(): También puedes usar el método update() para agregar múltiples
 elementos clave-valor de otro diccionario o de una secuencia de pares clave-valor
 (por ejemplo, una lista de tuplas).
python
Copy code
mi_diccionario = {}  # Crear un diccionario vacío
mi_diccionario.update({"clave1": "valor1", "clave2": "valor2"})  # Agregar múltiples elementos clave-valor
Aquí tienes ejemplos de ambas formas:

python
Copy code
# Crear un diccionario vacío
mi_diccionario = {}

# Agregar elementos clave-valor utilizando la notación de corchetes
mi_diccionario["nombre"] = "Juan"
mi_diccionario["edad"] = 30

# Imprimir el diccionario después de agregar elementos
print(mi_diccionario)

# Utilizar el método update() para agregar más elementos clave-valor
mi_diccionario.update({"ciudad": "México", "profesión": "Ingeniero"})

# Imprimir el diccionario después de agregar más elementos
print(mi_diccionario)
"""


frutas_precio = {}

while True:
    fruta = input("Ingrese fruta: ")
    precio = float(input(f"Ingrese precio de {fruta}: "))
    frutas_precio[fruta] = precio
    question = input("Responda solo si o no. Desea continuar ingresando frutas: ")
    if question.lower() == "no":
        break

print("El diccionario de frutas y sus precios es:")
print(frutas_precio)


















