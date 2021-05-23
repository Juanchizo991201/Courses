import os

password = "@Pnqeeec0"
password = password.lower() 
os.system("clear")
password2 = str(input("Digite su contraseña:\n"))
password2 = password2.lower()
os.system("clear")

if password == password2:
    print("las contraseñas coinciden")
else:
    print("las contraseñas no coinciden")