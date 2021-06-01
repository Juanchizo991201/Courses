import os

os.system("clear")

personalInfo = {}

llave = str(input("Digite el tipo de información que desea agregar :\n"))


while llave != "":   
    os.system("clear")   
    print("Digite su ", llave, ":")
    valor = str(input())
    if llave.capitalize() not in personalInfo.keys():
        personalInfo[llave.capitalize()] = valor.capitalize()
    else:
        os.system("clear")
        print("Este dato ya está en el diccionario")
    os.system("clear")
    llave = ""
    valor = ""    
    llave = str(input("Digite el tipo de información que desea agregar o enter para salir:\n"))

print(personalInfo)

