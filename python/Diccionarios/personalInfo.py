import os

os.system("clear")

# information = {"Nombre":"", "Eddad":"", "Dirección":"", "Telefono":""}
information = {}

print("digire su nombre:")
information["Nombre"] = str(input())
print("digire su edad:")
information["Edad"] = str(input())
print("digire su dirección:")
information["Dirección"] = str(input())
print("digire su teléfono:")
information["Teléfono"] = str(input())


print(information)