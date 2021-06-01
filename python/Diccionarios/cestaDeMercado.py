import os

os.system("clear")

productsDict = {}

llave = str(input("Digite el nombre del producto que desea agregar :\n"))


while llave != "":   
    os.system("clear")   
    print("Digite el precio del ", llave, ":")
    precio = float(input())
    if llave.capitalize() not in productsDict.keys():
        productsDict[llave.capitalize()] = precio
    os.system("clear")
    llave = ""
    precio = ""    
    llave = str(input("Digite el nombre del producto que desea agregar o enter para salir:\n"))

total = 0
for i, (key, value) in enumerate(productsDict.items()):
    print(key, "\t", value)
    total = total + float(value)

print("\nTotal \t", total)