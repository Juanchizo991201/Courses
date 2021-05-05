inputCodigo = ["| ||| |", "||  |||", "   |||||| ", "|| |||"]
# inputCodigo = ["| ||| |"]

stock = {'41': ['Manzana', 800], '302': ['Tamarino', 600], '6000': ['Papel h', 1500],
         '32': ['Café', 7500],  '5500': ['Tomate chonto', 3500]}

selected = []

for i in range(len(inputCodigo)):
    producto = (str(inputCodigo[i]))
    # print("\n", len(producto))
    barra = 0
    espacio = 0
    codigo = 0
    for j in range(len(producto)):

        if producto[j] == "|":
            barra = barra + 1
            # print("!!!", j, len(producto))
            if j == (len(producto)-1):
                mult = (barra * (10 ** espacio))
                # print("mult", mult)
                # print("c", codigo)

                codigo = codigo + mult
                # print("-> ", barra, espacio)

        else:
            # print(barra, espacio)
            if j > 0 and producto[j-1] == "|":
                mult = (barra * (10 ** espacio))
                # print("mult", mult)
                # print("c", codigo)
                codigo = codigo + mult
                # print("-> ", barra, espacio)
                barra = 0
                espacio = 0

            espacio = espacio + 1
    # print("Code: ", codigo, "\n")
    selected.insert(0, codigo)

# print(selected)

i = 0
totalPrice = 0
for i in range(len(selected)):
    try:
        stock [str(selected[i])]
        # print("Si existe")
        print(stock[str(selected[i])])
        item = (stock[str(selected[i])])
        
        totalPrice = totalPrice + int(item[1])
    except:
        print("No existe")


print("Total a pagar $:", totalPrice)