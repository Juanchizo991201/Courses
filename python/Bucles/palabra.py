import os
os.system("clear")

palabra = str(input("introduzca una palabra:\n"))
os.system("clear")
j = len(palabra)-1
for i in range(len(palabra)):    
    print(palabra[j])
    j = j - 1
