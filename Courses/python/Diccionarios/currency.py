import os

os.system("clear")

divisas = {"Euro":"€", "Dollar":"$", "Yen":"¥"}

moneda = str(input("Digite el nombre de la divisa:\n").capitalize())

os.system("clear")

try:
    print(divisas[str(moneda)])
except:
    print("La divisa no existe en el diccionario")