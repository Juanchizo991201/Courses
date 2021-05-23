import os

n = int(input("Digite un numero:\n"))
os.system("clear")

for i in range(n+1):
    if i%2 != 0:
        print(i)