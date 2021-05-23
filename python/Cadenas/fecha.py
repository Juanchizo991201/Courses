import os

fecha = str(input("Digite su fecha de nacimiento:\n")).split("/")
os.system("clear")

print("dia: ", fecha[0])
print("mes: ", fecha[1])
print("año: ", fecha[2])