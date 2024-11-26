import sys

# Definition of a Node
class Node:
    def __init__(self, nodename, startvalue):
        self.incomingConnections = []
        self.outgoingConnections = []
        self.nodeName = nodename
        self.ranking = []
        self.ranking.append(startvalue)

    def newconnection(self, incomingnode):
        self.incomingConnections.append(int(incomingnode))

    def debugnode(self):
        print("--- Debug of Node", self.nodeName, ":")
        print("Incoming Connections:", self.incomingConnections)
        print("Rankings:", self.ranking)
        print("--- End of Debug for Node", self.nodeName, "--- \n")


def initnodes():
    init_dampeningfactor = float(input("Was ist dein 'd' Wert?"))

    print("Debug: dampeningFactor = ", dampeningFactor) if debug else None

    # User gibt an, wie viele Nodes es gibt.
    # Aktuell ist 26 das Maximum, da die Nodes von A bis Z benannt werden sollte aber 100 % ausreichen
    nodeamount = int(input("Wie viele Nodes gibt es? (>= 2 & <= 26)"))
    initialvalue = int(input("Was soll der Startwert der Pageranks sein?"))
    for i in range(nodeamount):
        nametmp = str(input(f"Wie soll die {i+1}. Node heißen? (Node Namen dürfen nicht doppelt sein)"))
        nodetemp = Node(nametmp, initialvalue)
        nodedict[id(nodetemp)] = nodetemp
    return nodedict, init_dampeningfactor



def initconnections(newnodes):
    # TODO: input validation + error handling
    for nnode, node in newnodes.items():
        connectionamount = int(input(f"Wie viele eingehende Verbindungen hat Node '{node.nodeName}'?"))
        for j in range(connectionamount):
            node.newconnection(id(newnodes.get(input(f"Von wo stammt die {j + 1}. Verbindung zu Node {node.nodeName}?"))))
        if debug: node.debugnode()

    for nname, node in newnodes.items():
        for incoming in node.incomingConnections:
            newnodes.get(str(incoming)).outgoingConnections.append(incoming)

    return newnodes



def calculatepageranks(in_tocalc, in_nodedict, calc_dampeningfactor):
    backlinks = 0.0
    for i in range(1, in_tocalc + 1):
        for name, nodecon in in_nodedict.items():
            for j in nodecon.incomingConnections:
                 backlinks = backlinks + (in_nodedict.get(j).ranking[i-1] / len(in_nodedict.get(j).outgoingConnections))
            nodecon.ranking.append(( 1 - calc_dampeningfactor ) + calc_dampeningfactor * backlinks)
            backlinks = 0.0
    return in_nodedict


if __name__ == '__main__':
    nodedict = {}
    # Debug mode, wenn das Program mit der Flag "-debug" aufgerufen wird
    if "-debug" in sys.argv:
        debug = True
        print("Debug mode enabled")
    else:
        debug = False

    if "-defaults" in sys.argv:
        print("Default values enabled")
        tmphold1 = Node("FA", 0)
        nodedict[id(tmphold1)] = tmphold1
        tmphold2 = Node("FB", 0)
        nodedict[id(tmphold2)] = tmphold2
        tmphold3 = Node("FC", 0)
        nodedict[id(tmphold3)] = tmphold3
        dampeningFactor = 0.85
        tocalc = 15
        tmphold1.newconnection(id(tmphold2))
        tmphold2.newconnection(id(tmphold1))
        tmphold3.newconnection(id(tmphold1))
        tmphold3.newconnection(id(tmphold2))
        for defaults_i, defaults_j in nodedict.items():
            for incomingcons in defaults_j.incomingConnections:
                nodedict.get(incomingcons).outgoingConnections.append(incomingcons)

    else:
        nodedict, dampeningFactor = initnodes()
        nodedict = initconnections(nodedict)

        # TODO: ermitteln, wie oft der Pagerank iterativ berechnet werderen soll
        tocalc = int(input("Wie oft soll der Pagerank der Seiten iterativ berechnet werden?: "))

    # TODO: Iterative Berechnung des Pageranks -> Ergebnisse im Jeweiligen Node
    nodedict = calculatepageranks(tocalc, nodedict, dampeningFactor)

    print(tocalc)
    for foo in nodedict.values():
        print(f"{foo.nodeName}: {foo.ranking}")

    # TODO: Formatierte ausgabe der Ergebnisse
    # NTH: Möglichkeit die Eingabe nachzubessern
    # NTH: Nicht lineare Menüführung