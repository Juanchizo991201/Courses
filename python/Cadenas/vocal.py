import os

frase = str(input("Digite una frase\n"))
vocal = input("introduzca la vocal a volver mayuscula:\n")

os.system("clear")

i = 0

for i in range(len(frase)):
    if frase[i] == vocal:
        print(str(frase[i]).upper(), end="")
    else:
        print(frase[i], end="")

print("\n")