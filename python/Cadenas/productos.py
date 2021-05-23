import os

productos = str(input("Digite la lista de productos separados por coma:\n")).split(",")
os.system("clear")

cantidad = len(productos)

for i in range (cantidad):
    print(productos[i])
