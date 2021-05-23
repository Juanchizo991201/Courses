import os

os.system("clear")

dicionarioMeses = {"01":"Enero", "02":"Febrero", "03":"Marzo", "04":"Abril", "05":"Mayo", "06":"Junio", "07":"Julio", "08":"Agosto", "09":"Septiembre", "10":"Octubre", "11":"Noviembre", "12":"Diciembre"}

fecha = input("Digite la fecha en el formato dd/mm/aaaa:\n").split("/")

try:
    if int(fecha[0]) < 31 or int(fecha[1]) < 12:
        print(fecha[0], dicionarioMeses[str(fecha[1])], fecha[2])
    else:
        print("Fecha inválida")
except:
    print("Fecha inválida")


