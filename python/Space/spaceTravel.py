import os
target = ["Mars", "Saturn"]
routs = ["Sun Earth", "Mercury Venus", "Mars Mercury", "Mercury Saturn"]

origin = target[0]
destination = target[1]


class node:
    padre = None

    def __init__(self, padre=None, nombre=0):
        self.padre = padre
        self.nombre = nombre

    def __eq__(self, otro):
        return self.nombre == otro.nombre

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()


# Creacion de nodes y Conexiones con su padre
nodes = []
for i in range(len(routs)):
  ruta = routs[i].split(" ")
  node1 = node(nombre=ruta[0])
  node2 = node(node1.nombre, ruta[1])
  if node1 not in nodes:
    nodes.append(node1)
  if node2 not in nodes:
    nodes.append(node2)

  for j in range(len(nodes)):
    if node1 == nodes[j]:
      if nodes[j].padre == None:
        nodes[j] = node1
      elif (nodes[j].padre != node1.padre) and (node1.padre!=None):
        nodes.append(node1)
    
    if node2 == nodes[j]:
      if nodes[j].padre == None:
        nodes[j] = node2
      elif nodes[j].padre != node2.padre and (node2.padre!=None):
        nodes.append(node2)

print(nodes)

# Verificacion de las rutas incorrectas
posibles_rutas = []

for i in range(len(nodes)):
  ruta = []
  if nodes[i].padre == None:
    ruta.append(nodes[i])
    array = []
    for j in range(len(nodes)):
      if nodes[j].padre == ruta[-1].nombre:
        ruta.append(nodes[j])
      elif nodes[j].padre != None:
        if node(nombre=nodes[j].padre) in ruta:
          copia_ruta = ruta.copy()
          while copia_ruta[-1] != node(nombre=nodes[j].padre):
            copia_ruta.pop()
          copia_ruta.append(nodes[j])
          print(copia_ruta)
          posibles_rutas.append(copia_ruta.copy())
  
  if len(ruta)!=0:
    print(ruta)
    posibles_rutas.append(ruta)

# identificacion del objetivo
pos = 0

os.system("clear")

print("The wrong routs are:")

for ruta in posibles_rutas:
  decision = False
  for j in range(len(ruta)):
    if node(nombre=target[0]) == ruta[j]:
      for k in range(j,len(ruta)):
        if node(nombre=target[1]) == ruta[k]:
          decision=True

  if decision == False:
    print(ruta)