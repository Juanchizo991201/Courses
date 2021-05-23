import os
os.system("clear")

materias = ["Matemáticas", "Ingles", "Religión", "Química", "Sociales"]
notas = []

for i in range (len(materias)):
    os.system("clear")
    print("Digite la calificación que sacó en: ", materias[i], "\n")
    nota = float(input())     
    notas.insert(i, nota)

i = 0

for i in range (len(notas)):
    print("en ",materias[i]," sacó: ", notas[i])