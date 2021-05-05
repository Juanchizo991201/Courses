import os
os.system("clear")

array1 = [1, 2, 3]
array2 = [-1, 0, 2]

answ = []
suma = 0
for i in range (len(array1)):
    mult = int(array1[i]) * int(array2[i])
    answ.insert(i, mult)
    suma = suma + mult

print("El producto del vector es: ", suma)