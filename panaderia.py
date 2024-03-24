#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un 
#descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas
#que no son del día. Después el programa debe mostrar el precio habitual de una 
#barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

standar_price = 1000
old_bread_sold = int(input("Ingrese cantidad de barras de pan no frescas vendidas: "))

print(f"El precio habitual de una barra de pan es de: ${standar_price}")
print(f"El descuento q se hace por no ser fresca es de: ${(standar_price - (standar_price / 1.60) ):.2f}")
print(f"El coste final por barra no fresca es de ${(standar_price / 1.60):.2f}")
print(f"El coste final por las ${old_bread_sold} barras no frescas vendidas es de ${((standar_price / 1.60) * old_bread_sold ):.2f}")
