import os
os.system("clear")

oracion = str(input("introdzca un oración:\n"))
letra = str(input("introduzca una letra:\n"))

while len(letra) != 1:
    print("debe digitar solo una letra\n")
    letra = str(input("introduzca una letra:\n"))

contador = 0

for i in range (len(oracion)):
    if letra == oracion[i]:
        contador = contador + 1

print("la letra: ",letra, " se repite ",contador," veces")