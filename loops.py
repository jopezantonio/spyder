"""
Aplicación 03: Suma de n números anteriores
Enunciado: obtener la suma de los primeros N número 
natural positivo.

Análisis: Para la solución de este problema,
se requiere que el usuario ingrese un número y el
sistema realice el proceso para devolver la suma de
los N primeros números."""

n = 3
print(n)
sum = 0

while n <=3:
    sum += n
    n -= 1
    print(sum)
