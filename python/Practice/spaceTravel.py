import os
target = ["Mars", "Saturn"]
routs = ["Sun Earth", "Mercury Venus", "Mars Mercury", "Mercury Saturn"]

origin = target[0]
destination = target[1]


class node:
    father = None

    def __init__(self, father=None, name=0):
        self.father = father
        self.name = name

    def __eq__(self, otro):
        return self.name == otro.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


nodes = []
for i in range(len(routs)):
    rout = routs[i].split(" ")
    node1 = node(name=rout[0])
    node2 = node(node1.name, rout[1])
    if node1 not in nodes:
        nodes.append(node1)
    if node2 not in nodes:
        nodes.append(node2)

    for j in range(len(nodes)):
        if node1 == nodes[j]:
            if nodes[j].father == None:
                nodes[j] = node1
            elif (nodes[j].father != node1.father) and (node1.father != None):
                nodes.append(node1)

        if node2 == nodes[j]:
            if nodes[j].father == None:
                nodes[j] = node2
            elif nodes[j].father != node2.father and (node2.father != None):
                nodes.append(node2)

print(nodes)


possible_routs = []

for i in range(len(nodes)):
    rout = []
    if nodes[i].father == None:
        rout.append(nodes[i])
        array = []
        for j in range(len(nodes)):
            if nodes[j].father == rout[-1].name:
                rout.append(nodes[j])
            elif nodes[j].father != None:
                if node(name=nodes[j].father) in rout:
                    routCopy = rout.copy()
                    while routCopy[-1] != node(name=nodes[j].father):
                        routCopy.pop()
                    routCopy.append(nodes[j])
                    print(routCopy)
                    possible_routs.append(routCopy.copy())

    if len(rout) != 0:
        print(rout)
        possible_routs.append(rout)

os.system("clear")

print("The wrong routs are:")

for rout in possible_routs:
    decision = False
    for j in range(len(rout)):
        if node(name=target[0]) == rout[j]:
            for k in range(j, len(rout)):
                if node(name=target[1]) == rout[k]:
                    decision = True

    if decision == False:
        for i in range(len(rout)):
            if i != len(rout)-1:
                print(rout[i], end=" -> ")
            else:
                print(rout[i])

