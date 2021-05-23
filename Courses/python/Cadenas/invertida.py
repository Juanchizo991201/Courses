import os

frase = str(input("Digite una frase\n"))
os.system("clear")

j = len(frase)-1

for i in range(len(frase)):
    print(frase[j], end="")
    j = j-1

print("\n")
