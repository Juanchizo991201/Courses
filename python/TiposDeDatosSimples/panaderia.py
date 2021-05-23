import os

precioBarra = 3.49
descuento = 60/100

barras = int(input("Digite el numero de barras que no estan frescas:\n"))
os.system("clear")
print("El valor de una barra fesca es de:\n", precioBarra, "€")
print("El valor del descuento es de:\n", precioBarra*barras*descuento, "€")
print("El valor total del pan con descuento es de:\n", round(precioBarra*barras*(1-descuento), 2), "€")
