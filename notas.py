# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 01:55:36 2024

@author: PC
"""

asignaturas = ("Matemáticas", "Física", "Química", "Historia", "Lengua")
notas = []
i = 0

for asignatura in asignaturas:
    nota = int(input( f"Ingrese nota de {asignatura}: "))
    notas.append(nota)
    
print("\n")
print("\n")
print("*" * 50)
    
for asignatura, nota in zip(asignaturas, notas):
    print(f"{asignatura}: {nota}")



"""
OJOOOOOO Es muy util el elemento zip() utilizado arriba, este combina dos o mas iterables
sean listas o tuplas o cualquier iterable. En el ejemplo arriba vemos como combina la tupla
asignaturas y la lista notas. Aca se uso un ciclo for la sintaxis se explica asi
for asignatura, nota in zip(asignaturas, notas):
    asignatura  y nota son los nombres q se le da a cada elemento de la lista al 
    iterar pero pudiera ser cualquiera:
        for x, y in zip(asignaturas, notas): denro del parentesis del metodo
        zip estan los iterables en este caso la tupla asignaturas y la lista 
        notas.  Asi en cada iteracion x va a ser el valor de asignaturas va desde
        el indice 0 q es matematicas hasta el ultimo q es lengua y y hace lo mismo
        pero en la lista notas


    """