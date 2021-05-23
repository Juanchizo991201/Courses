import os

ingresos = float(input("Digite el valor de ingresos que tiene:\n"))

if ingresos < 10000:
    print("le corresponde el 5%")
elif ingresos >= 10000 and ingresos < 20000:
    print("le corresponde el 15%")
elif ingresos >= 20000 and ingresos < 35000:
    print("le corresponde el 20%")
elif ingresos >= 35000 and ingresos < 60000:
    print("le corresponde el 30%")
else:
    print("le corresponde el 45%")