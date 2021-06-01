import os

os.system("clear")

diccionarioEspEng = {}

palabra = str(input("Digite las palabras a agregar en el diccioanrio de la forma Esañol:Ingles \n"))
try:
    palabra_traduccion = palabra.split(":") 
    if palabra_traduccion [0] != "" and palabra_traduccion [1] != "":
        if palabra_traduccion [0] not in diccionarioEspEng.keys():        
            diccionarioEspEng [palabra_traduccion[0]] = palabra_traduccion[1]
    else:
        print("Palabra invalida")
except:
    print("Palabra invalida")



while palabra != "":
    os.system("clear")
    palabra = ""
    palabra = str(input("Digite las palabras a agregar en el diccioanrio de la forma Esañol:Ingles o presione enter para seguir\n"))
    palabra_traduccion = palabra.split(":") 
    try:
        palabra_traduccion = palabra.split(":") 
        if palabra_traduccion [0] != "" and palabra_traduccion [1] != "":
            if palabra_traduccion [0] not in diccionarioEspEng.keys():        
                diccionarioEspEng [palabra_traduccion[0]] = palabra_traduccion[1]
            else:
                print("la palabra ya está en el diccionario")
        else:
            print("Palabra invalida")
    except:
        print("Palabra invalida")

os.system("clear")

# print(diccionarioEspEng)

frase = str(input("Digite la frase a traducir:\n")).split(" ")

os.system("clear")

for i in range (len(frase)):
    try:
        print(diccionarioEspEng[frase[i]])
    except:
        print(frase[i])
