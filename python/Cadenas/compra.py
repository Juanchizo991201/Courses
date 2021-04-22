import os

producto = str(input("Digite el nombre del producto:\n"))
precio = float(input("Digite el precio del producto:\n"))
unidades = int(input("Digite la cantidad de unidades:\n"))

print(producto, " - ",precio, " - ", unidades, " - valor total: ", precio*float(unidades))