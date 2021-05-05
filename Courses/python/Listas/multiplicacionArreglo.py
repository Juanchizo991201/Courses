import os

os.system("clear")

array1 = str("(1 2 3 4 5 6)")
array2 = str("(-1 0 0 1 1 1)")


list1 = []
list2 = []

contador1 = 0
negativo = False

for i in range(len(array1)):

    if ord(str(array1[i])) >= 48 and ord(str(array1[i])) <= 57:
        if negativo == False:
            list1.insert(contador1, int(array1[i]))
            contador1 += 1
        else:
            negativo = False
    elif ord(str(array1[i])) == 45:
        list1.insert(contador1, int(array1[i+1])*-1)
        contador1 += 1
        negativo = True

contador1 = 0
negativo = False

for i in range(len(array2)):

    if ord(str(array2[i])) >= 48 and ord(str(array2[i])) <= 57:
        if negativo == False:
            list2.insert(contador1, int(array2[i]))
            contador1 += 1
        else:
            negativo = False
    elif ord(str(array2[i])) == 45:
        list2.insert(contador1, int(array2[i+1] )* -1)
        contador1 += 1
        negativo = True

result = []

for i in range (len(list1)):
    result.insert(i, (list1[i] *  list2[i]))

print(result)