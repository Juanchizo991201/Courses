import os
os.system("clear")

line = str(input("Introduzca un texto cualquiera o escriba salir para terminar:\n"))

while line != str("salir"):
    os.system("clear")
    print(line)
    line = str(input())
    