import os
os.system("clear")

materias = ["Matemáticas", "Ingles", "Religión", "Química", "Sociales"]
notas = []

for i in range (len(materias)):
    os.system("clear")
    print("Digite la calificación que sacó en: ", materias[i])
    nota = float(input())     
    notas.insert(i, nota)

i = 0

print(materias)
print(notas)

for i in range (len(notas)):
    if float(notas[i]) >= 3.0:
        materias[i] = None
    
i = 0

os.system("clear")

print("las materias que debe repetir son:")

for i in range (len(materias)):
    if materias[i] != None:
        print(materias[i])