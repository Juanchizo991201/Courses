import os
os.system("clear")

numeros = []
numero = 0
while (numero) != str(""):
    try:
        numero = int(input("Digite el valor de la lotería:\n"))
        numeros.insert(0, numero)
    except:
        break

numeros.sort()

print("Los numeros ganadores son: ", numeros)