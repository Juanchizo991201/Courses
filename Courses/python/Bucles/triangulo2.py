import os

n = int(input("introduzca un número:\n"))

os.system("clear")

for i in range (n):
    n = (i+1)    
    if n%2 != 0:
        for j in range (n):
            if j%2 == 0:
                print(n,end="\t")
                n = n-2
    print("")