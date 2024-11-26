import sys
from Node import Node

def initnodes():
    init_dampeningfactor = float(input("Was ist dein 'd' Wert?"))

    print("Debug: dampeningFactor = ", Dampeningfactor) if Debug else None

    # User gibt an, wie viele Nodes es gibt.
    nodeamount = int(input("Wie viele Nodes gibt es? (>= 2 & <= 26)"))
    initialvalue = int(input("Was soll der Startwert der Pageranks sein?"))
    for i in range(nodeamount):
        nametmp = str(input(
            f"Wie soll die {i+1}. Node heißen? (Node Namen dürfen nicht doppelt sein)"
        ))
        nodetemp = Node(nametmp, initialvalue)
        nodedict[id(nodetemp)] = nodetemp
    return nodedict, init_dampeningfactor

def createnamemapping(dict_tomap):
    mappeddict = {}
    for nodeid, node in dict_tomap.items():
        mappeddict[node.nodeName] = nodeid
    return mappeddict

def initconnections(newnodes):
    mapping = createnamemapping(newnodes)
    for node in newnodes.values():
        connectionamount = int(
            input(f"Wie viele eingehende Verbindungen hat Node '{node.nodeName}'?")
        )
        for j in range(connectionamount):
            node.newconnection(mapping.get(
                input(f"Von wo stammt die {j + 1}. Verbindung zu Node {node.nodeName}?")
            ))
        if Debug: node.debugnode()

    for node in newnodes.values():
        for incoming in node.incomingConnections:
            newnodes.get(incoming).outgoingConnections.append(incoming)

    return newnodes



def calculatepageranks(in_tocalc, in_nodedict, calc_dampeningfactor):
    backlinks = 0.0
    for i in range(1, in_tocalc + 1):
        for nodecon in in_nodedict.values():
            for j in nodecon.incomingConnections:
                backlinks = (backlinks +
                             (in_nodedict.get(j).ranking[i-1]
                              / len(in_nodedict.get(j).outgoingConnections)))
            nodecon.ranking.append(( 1 - calc_dampeningfactor ) +
                                   calc_dampeningfactor * backlinks)
            backlinks = 0.0
    return in_nodedict


if __name__ == '__main__':
    # Debug mode, wenn das Program mit der Flag "-debug" aufgerufen wird
    if "-debug" in sys.argv:
        Debug = True
        print("Debug mode enabled")
    else:
        Debug = False

    nodedict = {}

    if "-defaults" in sys.argv:
        print("Default values enabled")
        tmphold1 = Node("FA", 0)
        nodedict[id(tmphold1)] = tmphold1
        tmphold2 = Node("FB", 0)
        nodedict[id(tmphold2)] = tmphold2
        tmphold3 = Node("FC", 0)
        nodedict[id(tmphold3)] = tmphold3
        Dampeningfactor = 0.85
        tocalc = 15
        tmphold1.newconnection(id(tmphold2))
        tmphold2.newconnection(id(tmphold1))
        tmphold3.newconnection(id(tmphold1))
        tmphold3.newconnection(id(tmphold2))
        for defaults_i, defaults_j in nodedict.items():
            for incomingcons in defaults_j.incomingConnections:
                nodedict.get(incomingcons).outgoingConnections.append(incomingcons)

    else:
        nodedict, Dampeningfactor = initnodes()
        nodedict = initconnections(nodedict)

        tocalc = int(input("Wie oft soll der Pagerank der Seiten iterativ berechnet werden?: "))

    nodedict = calculatepageranks(tocalc, nodedict, Dampeningfactor)

    print(tocalc)
    for foo in nodedict.values():
        print(f"{foo.nodeName}: {foo.ranking}")
