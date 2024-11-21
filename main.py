import sys

nodeNames = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nodedict = {}
dampeningFactor = 0.0
backlinks = 0.0


# Definition of a Node
class Node:
    def __init__(self, name, startvalue):
        self.incomingConnections = []
        self.outgoingConnections = []
        self.nodeName = name
        self.ranking = []
        self.ranking.append(startvalue)

    def newconnection(self, incomingnode):
        self.incomingConnections.append(incomingnode)

    def debugnode(self):
        print("--- Debug of Node", self.nodeName + ":")
        print("Incoming Connections:", self.incomingConnections)
        print("Rankings:", self.ranking)
        print("--- End of Debug for Node", self.nodeName, "--- \n")


def initnodes():
    global dampeningFactor
    global nodedict # Die Node Instanzen werden in einer globalen Liste gespeichert
    # User gibt den dampening Faktor d an TODO: input validation + error handling
    dampeningFactor = float(input("Was ist dein 'd' Wert?"))

    print("Debug: dampeningFactor = ", dampeningFactor) if debug else None

    # User gibt an, wie viele Nodes es gibt.
    # Aktuell ist 26 das Maximum, da die Nodes von A bis Z benannt werden sollte aber 100 % ausreichen
    nodeamount = int(input("Wie viele Nodes gibt es? (>= 2 & <= 26)"))
    initialvalue = int(input("Was soll der Startwert der Pageranks sein?"))
    for i in range(nodeamount):
        nodedict[nodeNames[i]] = Node(nodeNames[i], initialvalue)
    return nodedict



def initconnections(newnodes):
    # TODO: input validation + error handling
    for node in newnodes.values():
        connectionamount = int(input("Wie viele eingehende Verbindungen hat Node '" + node.nodeName + "'"))
        for j in range(connectionamount):
            node.newconnection(input(f"Von wo stammt die {j + 1}. Verbindung zu Node {node.nodeName}?"))
        if debug: node.debugnode()

    for nname, node in newnodes.items():
        for incoming in node.incomingConnections:
            nodedict.get(incoming).outgoingConnections.append(incoming)



def calculatepageranks(in_tocalc, in_nodedict):
    global backlinks
    for i in range(1, in_tocalc + 1):
        for name, nodecon in in_nodedict.items():
            for j in nodecon.incomingConnections:
                 backlinks = backlinks + (in_nodedict.get(j).ranking[i-1] / len(in_nodedict.get(j).outgoingConnections))
            nodecon.ranking.append(( 1 - dampeningFactor ) + dampeningFactor * backlinks)
            backlinks = 0.0
    return in_nodedict


if __name__ == '__main__':
    # Debug mode, wenn das Program mit der Flag "-debug" aufgerufen wird
    if "-debug" in sys.argv:
        debug = True
        print("Debug mode enabled")
    else:
        debug = False

    nodedict = initnodes()
    initconnections(nodedict)

    # TODO: ermitteln, wie oft der Pagerank iterativ berechnet werderen soll
    tocalc = int(input("Wie oft soll der Pagerank der Seiten iterativ berechnet werden?: "))

    # TODO: Iterative Berechnung des Pageranks -> Ergebnisse im Jeweiligen Node
    nodedict = calculatepageranks(tocalc, nodedict)

    print(tocalc)
    for foo in nodedict.values():
        print(f"{foo.nodeName}: {foo.ranking}")

    # TODO: Formatierte ausgabe der Ergebnisse
    # NTH: Möglichkeit die Eingabe nachzubessern
    # NTH: Nicht lineare Menüführung