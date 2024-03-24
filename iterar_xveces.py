#Escribir un programa que pregunte el nombre del usuario en la consola y un número 
#entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces 
#como el número introducido.
name =  input("Ingrese su nombre: ")
number = int(input("Ingrese un numero entero: "))
for _ in range(number):
    print(f"Hola, {name.lower()}")