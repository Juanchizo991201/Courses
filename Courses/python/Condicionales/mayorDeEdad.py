import os

edad = int(input("Digite su edad:\n"))
os.system("clear")

if edad < 18:
    print("El individuo es menor de edad")
else:
     print("El sujeto es mayor de edad")