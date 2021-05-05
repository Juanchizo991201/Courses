import os
os.system("clear")

n = int(input("digite un número:\n"))

if n % 2 == 0 and n/2 != 1:
    print("multiplo de  2")
else:
    if n % 3 == 0 and n/3 != 1:
        print("multiplo de  3")
    else:
        if n % 5 == 0 and n/5 != 1:
            print("multiplo de  5")
        else:
            if n % 7 == 0 and n/7 != 1:
                print("multiplo de  7")
            else:
                print("Numero Primo")
    

