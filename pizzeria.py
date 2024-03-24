# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 05:59:55 2024

@author: PC
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

print("*" * 25, "PIZZERIA BELLA NAPOLI", "*" * 25, "\n")

print("*" * 28, "MENU DE PIZZAS", "*" * 28, "\n" * 2)

print("Opcion 1. Pizza Vegetariana", "\n" * 2)
print("Opcion 2. Pizza No Vegetariana", "\n" * 2)

pizza = int(input("///////Ingrese el numero de opcion deseado y presione enter: "))
print("\n")
print("\n")
print("\n")
print("\n")
base = ["tomate", "mozzarella"]

if pizza >= 1 and pizza <= 2:
    if pizza == 1:
        print("La pizza tiene el tomate y el mozzarella incluido", "\n")
        print("Puede escoger un ingrediente adicional. Ingrese la opcion deseada y presione enter")
        print("Opcion 1. Pimiento")
        print("Opcion 2. Tofu")
        adicional = int(input("///////Ingrese el numero de opcion deseado y presione enter: "))
        if adicional == 1:
            base.append("pimiento")
            print(f"Su orden es una pizza vegetariana con {base}")
        else:
            base.append("tofu")
            print(f"Su orden es una pizza vegetariana con {base}")
            
    else:
        print("La pizza tiene el tomate y el mozzarella incluido", "\n")
        print("Puede escoger un ingrediente adicional. Ingrese la opcion deseada y presione enter")
        print("Opcion 1. Pepperoni")
        print("Opcion 2. Jamon")
        print("Opcion 3. Salmon")
        adicional = int(input("///////Ingrese el numero de opcion deseado y presione enter: "))
        if adicional == 1:
            base.append("Pepperoni")
            print(f"Su orden es una pizza no vegetariana con {base}")
        elif adicional == 2:
            base.append("Jamon")
            print(f"Su orden es una pizza no vegetariana con {base}")
        else:
            base.append("Salmon")
            print(f"Su orden es una pizza no vegetariana con {base}")
else:
    print("Opcion no permitida, escoga solo una de las opciones ofrecidas en el menu")






