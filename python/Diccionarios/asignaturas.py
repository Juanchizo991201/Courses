import os

os.system("clear")

diccionarioCreditos = {"Matematicas":"4", "Español":"2", "Ingles":"3"}

for i, (key, value) in enumerate(diccionarioCreditos.items()):
    
    print("La asignatura ", key, " cuenta con ", value, "creditos.")
    