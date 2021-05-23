import os

precio = str(input("Introduzca el valor del producto:\n")).split(".")
os.system("clear")
print("son: ", precio[0], "€ y ", str(precio[1])[0:2], "centimos")
