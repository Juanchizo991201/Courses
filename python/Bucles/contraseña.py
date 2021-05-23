import os
os.system("clear")
keyword = str("contraseña")
password = str(input("introduzca su contraseña:\n"))

while keyword != password:
    os.system("clear")
    print("contraseña incorrecta, intente de nuevo\n")
    password = str(input("introduzca su contraseña: "))

print("Contraseña correcta")