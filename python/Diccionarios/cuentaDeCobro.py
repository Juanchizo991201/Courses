import os
import time

os.system("clear")

billDictionary = {}

option = str(input("Digite una option:\n1. Añadir una factura\n2. Pagar una factura\n3. Salir\n\n\n"))

billNumber = 0
billCost = 0

while option != "":
    
    os.system("clear")

    if option == "1":
        os.system("clear")
        print("Agregar factura\n\n")

        print("Digite el numero de de factura a agregar:")
        billNumber = int(input())
        print("Digite el valor de de factura a agregar:")
        billCost = float(input())

        billDictionary[billNumber] = billCost
        print("Añadiendo...")
        time.sleep(1)      

    elif option == "2" and len(billDictionary) != 0 :
        os.system("clear")
        print("Pagar factura\n\n")
        print("Digite el numero de de factura a pagar:")
        billNumber = int(input())

        try:
            billDictionary[billNumber]
        except:
            print("El nuemro de factura ingresado no corresponde, intene nuevemente")
            break

        print("La factura tiene un saldo de:", billDictionary[billNumber])       
        print("Digite el valor a cancelar")
        billCost = float(input())
        if billCost <= billDictionary[billNumber]:
            if billCost == billDictionary[billNumber]:
                billDictionary.pop(billNumber)
                print("pagando...")
                time.sleep(1)
            else:
                newbillcost = billDictionary[billNumber] - billCost
                billDictionary[billNumber] = newbillcost
                print("El nuevo saldo es de:\n", billDictionary[billNumber])
                print("pagando...")
                time.sleep(1)            
        else:
            print("El valor a cancelar es mayor al saldo")
            time.sleep(1)

    elif option == "3":
        os.system("clear")
        print("saliendo ...\n\n")
        break
    else:
        os.system("clear")
        print("Opción inválida\n\n")
    
    option = ""
    os.system("clear")
    option = str(input("Digite una option:\n1. Añadir una factura\n2. Para pagar una factura\n3. Salir\n"))

print(billDictionary)