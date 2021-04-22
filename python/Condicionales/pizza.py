import os


diccionario = {'V': 'Vegetariana', 'C': 'No Vegetariana', 'Pi': 'Pimineta',
               'T': 'Tofu', 'Pe': 'Peperoni', 'J': 'Jamón', 'S': 'Salmón', 'M': 'Mozzarella', 'SM': 'Sin Mozzarella'}

lista = []

opcion1 = input("Para ingredientes vegetarianos oprima V: \nPara ingredientes no vegetarianos oprima C:\n")
os.system("clear")
if opcion1 == "V" or opcion1 == "v":
    lista.insert(0, diccionario['V'])
    opcion2 = input("Para Pimiento oprima P: \nPara Tofu oprima T:\n")
    if opcion2 == "P" or opcion2 == "p":
        lista.insert(1, diccionario['Pi'])
        opcion3 = input("¿Desea agregar Mozzarella? S / N\n")
        if opcion3 == "S" or opcion3 == "s":
            lista.insert(2, diccionario['M'])
        else:
            lista.insert(2, diccionario['SM'])
    elif opcion2 == "T" or opcion2 == "t":
        lista.insert(1, diccionario['T'])
        opcion3 = input("¿Desea agregar Mozzarella? S / N\n")
        if opcion3 == "S" or opcion3 == "s":
            lista.insert(2, diccionario['M'])
        else:
            lista.insert(2, diccionario['SM'])
else:
    lista.insert(0, diccionario['C'])
    opcion2 = input("Para Peperoni oprima P:\nPara Jamón oprima J:\nPara salmón oprima S:\n")
    if opcion2 == "P" or opcion2 =="p":
        lista.insert(1, diccionario['Pe'])
        opcion3 = input("¿Desea agregar Mozzarella? S / N\n")
        if opcion3 == "S" or opcion3 == "s":
            lista.insert(2, diccionario['M'])
    elif opcion2 == "J" or opcion2 =="j":
        lista.insert(1, diccionario['J'])
        opcion3 = input("¿Desea agregar Mozzarella? S / N\n")
        if opcion3 == "S" or opcion3 == "s":
            lista.insert(2, diccionario['M'])
    elif opcion2 == "S" or opcion2 =="s":
        lista.insert(1, diccionario['S'])
        opcion3 = input("¿Desea agregar Mozzarella? S / N\n")
        if opcion3 == "S" or opcion3 == "s":
            lista.insert(2, diccionario['M'])

os.system("clear")
print("Los ingredientes de su pizza son:")
i = 0
for i in range(len(lista)):
    print(str(lista.pop(0)))
