import os

edad = int(input("Digite su edad:\n"))

if edad < 4:
    print("gratis")
elif edad >= 4 and edad < 18:
    print("pague 5€")
else:
    print("le corresponde el 10€")