import os

os.system("clear")

diccionarioProductos = {"Platano":"1.35", "Manzana":"0.80", "Pera":"0.85", "Naranja":"0.70"}

producto = str(input("Digite el nombre de producto:\n")).capitalize()
peso = float(input("Digite el peso:\n"))

try:
    precio = float(diccionarioProductos[producto]) * peso
    print("El precio de ", peso, " de ", producto, "Kg es de: $", precio)
except:
    print("no existe el producto")


