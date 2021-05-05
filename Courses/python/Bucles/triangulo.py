import os

n = int(input("introduzca un número:\n"))

os.system("clear")

for i in range (n+1):
    for j in range (i):
        print("*",end="")
    print("")