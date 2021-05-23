import os

nombre = input("Digite su nombre:\n")
n = int(input("Digite el numero de veces que desea escribir su nombre:\n"))

os.system("clear")

for i in range(n):
    print(nombre)