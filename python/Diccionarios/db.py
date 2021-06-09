import os
import time

os.system("clear")


personalInfoDicionary = {}
infoDictionary = {}

option = str(input("Digite una option:\n1. Añadir cliente\n2. Eliminar cliente\n3. Mostrar cliente\n4. Listar todos los clientes\n5. Listar clientes preferenciales\n6. Terminar\n\n\n"))

while option != "":
    os.system("clear")

    if option == "1":
        os.system("clear")
        print("Añadir cliente\n\n")

        try:
            nif = int(input("Digite el numero unico de identificación:\n\n"))
            os.system("clear")
        except:
            os.system("clear")
            print("Numero de identifiación invalido")
            nif = 0
            time.sleep(2)
        
        if nif != 0:
            nombre = str(input("Digite el nombre:\n\n")).capitalize()
            os.system("clear")
            direccion = str(input("Digite la dirección:\n\n"))
            os.system("clear")
            telefono = str(input("Digite el telefono:\n\n"))
            os.system("clear")
            correo = str(input("Digite el correo:\n\n"))
            os.system("clear")
            preferente = int(input("Digite 1 si es preferente, o 0 si no lo es:\n\n"))
            os.system("clear")
            try:
                if int(preferente) == 0 or int(preferente) == 1:
                    print()
                
            except:
                preferente = 10
                print("valor de preferencia invalido, vuelva a añadir al cliente")
                time.sleep(3)

            if preferente < 2:
                infoDictionary["nombre"] = nombre
                infoDictionary["direccion"] = direccion
                infoDictionary["telefono"] = telefono
                infoDictionary["correo"] = correo
                infoDictionary["preferente"] = preferente

                personalInfoDicionary[nif] = infoDictionary

                print("Añadiendo...")
                time.sleep(1)
            else:
                print("valor de preferencia invalido, vuelva a añadir al cliente")
                time.sleep(1)

    elif option == "2":
        os.system("clear")
        print("Eliminar cliente\n\n")

        if len(personalInfoDicionary) > 0:
            nif = int(
                input("Digite el numero unico de identificación del cliente a eliminar:\n\n"))
            os.system("clear")

            try:
                personalInfoDicionary.pop(nif)
                print("Eliminando...")
                time.sleep(1)
            except:
                print(
                    "El numero de identificación ingresado, no se encuentra en la base de datos")
                time.sleep(1)

        else:
            print("No hay clientes para ejecutar esta operación")
            time.sleep(1)

    elif option == "3":
        os.system("clear")
        print("Mostrar cliente\n\n")

        if len(personalInfoDicionary) > 0:
            nif = int(
                input("Digite el numero unico de identificación del cliente:\n\n"))
            os.system("clear")

            try:
                infoDictionary = personalInfoDicionary.get(nif)
                print(infoDictionary)
                print("NIF: ", nif)
                print("Nombre: ", infoDictionary["nombre"])
                print("Dirección: ", infoDictionary["direccion"])
                print("Teléfono: ", infoDictionary["telefono"])
                print("Correo: ", infoDictionary["correo"])
                if infoDictionary["preferente"] == 1:
                    print("Si es preferene")
                else:
                    print("No es preferene")
                time.sleep(5)
            except:
                print(
                    "El numero de identificación ingresado, no se encuentra en la base de datos")
                time.sleep(1)

        else:
            print("No hay clientes para ejecutar esta operación")
            time.sleep(2)

    elif option == "4":
        os.system("clear")
        print("Listar todos los clientes\n\n")

        if len(personalInfoDicionary) > 0:

            keys = list(personalInfoDicionary.keys())
            print(keys)
            time.sleep(2)

            # for i in range(len(keys)):
            #     infoDictionary = personalInfoDicionary[int(keys.pop)]
            #     print(infoDictionary)
            #     time.sleep(1)
            
        else:
            print("No hay clientes para ejecutar esta operación")
            time.sleep(1)

    elif option == "5":
        os.system("clear")
        print("Listar clientes preferenciales\n\n")

    elif option == "6":
        os.system("clear")
        print("Terminando...\n\n")
        time.sleep(1)
        break
    else:
        os.system("clear")
        print("Opción inválida\n\n")

    option = ""
    os.system("clear")
    option = str(input("Digite una option:\n1. Añadir cliente\n2. Eliminar cliente\n3. Mostrar cliente\n4. Listar todos los clientes\n5. Listar clientes preferenciales\n6. Terminar\n\n\n"))
