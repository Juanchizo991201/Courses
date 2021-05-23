import os

payasos = int(input("Digite el numero de payasos en el pedido:\n"))
os.system("clear")
muñecas = int(input("Digite el numero de muñecas en el pedido:\n"))
os.system("clear")

print("El peso total del pedido es de:\n", ((payasos*112)+(muñecas*75)), "g")