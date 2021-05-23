import os
os.system("clear")

abc = []

for i in range (122-96):
    abc.insert(i,chr(i+97))

print(abc)

i = 0

print(len(abc))
pos = 0
for i in range (len(abc)):
    pos = i +  1
    if pos % 3 == 0:
        abc.remove(chr(pos+96))

print(abc)