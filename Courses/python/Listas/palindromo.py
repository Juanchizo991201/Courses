import os
os.system("clear")

word = str(input("Digite una palabra:\n"))

right = []
revez = []

for i in range (len(word)):
    right.insert(i, word[i])
    revez.insert(0, word[i])

for j in range (len(right)):
    if str(right[j]) == str(revez[j]):
        if j == (len(right)-1):
            print("Si es palindorma")
        
    else:
        print("No es palindorma")
        break


