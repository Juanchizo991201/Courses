import os

interes = 4/100
deposito = float(input("Digite el valor del depósito inicial:\n"))

os.system("clear")

deposito = deposito + (deposito*interes)
print("El valor de interes en el primer año es de:\n", deposito)
deposito = deposito + (deposito*interes)
print("El valor de interes en el primer año es de:\n", deposito)
deposito += deposito + (deposito*interes)
print("El valor de interes en el primer año es de:\n", deposito)