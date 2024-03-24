frase = input("Introduzca una frase: ")
vocal = input("Introduzca una vocal: ")

# Reemplazar todas las ocurrencias de la vocal con su versión en mayúsculas
resultado = frase.replace(vocal, vocal.upper())

# Imprimir el resultado
print(resultado)