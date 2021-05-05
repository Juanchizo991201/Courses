import os

capital = float(input("digite el valor del dinero a invertir:\n"))
os.system("clear")
interes = float(input("Digite el valor de la tasa de interes:\n"))
os.system("clear")
años = float(input("Digite el numeo de años de la inversión:\n"))
os.system("clear")

print("El valor total a resivir de la inversión es de:\n", (capital*pow((1+(interes/100)),años)))