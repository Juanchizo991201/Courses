import os

n = int(input("Digite el divisor:\n"))
os.system("clear")
m = int(input("Digite el dividendo:\n"))
os.system("clear")

print("El divisor es:\n", n)  
print("El dividendo es:\n", m)  
print("El cociente es:\n", int(n/m))  
print("El resto es:\n", (n%m))  