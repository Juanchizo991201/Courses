import os

edad = int(input("Digite su edad:\n"))
ingresos = int(input("Digite el valor de sus ingresos:\n"))

if edad > 16:
    if ingresos >= 1000:
        print("si debe pagar impuestos")
    else:
        print("no debe pagar impuestos")
else:
    print("no debe pagar impuestos")
