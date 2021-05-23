import os

nombre = input("Digite su nombre:\n")
nombreSeparado = nombre.split(" ")
os.system("clear")

a = 0
for i in nombreSeparado:
    a=a+1
    
print("Su nombre tiene: ",len(nombre)-(a-1))