import os

capital = float(input("Digite la cantidad de dinero a invertir:\n"))
os.system("clear")
tasa = float(input("Digite el porcentaje de la tasa anual:\n"))
os.system("clear")
años = float(input("digite el numero de años que durará la inversión:\n"))
os.system("clear")

dinero = capital

for i in range (int(años)):
    dinero = dinero + dinero * (tasa/100)
    print("el dinero en el año ", (i+1), "es de: ", dinero)