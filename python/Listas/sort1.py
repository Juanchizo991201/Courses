import os
os.system("clear")

numbers = []

for i in range (10):
    numbers.insert(i, i+1)

i = 0

for i in range (len(numbers)):
    if i < (10-1):
        print(numbers.pop(), end=", ")
    else:
        print(numbers.pop())

