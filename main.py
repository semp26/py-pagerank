import sys


nodeNames = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nodelist = []
dampeningFactor = 0.0


# definition of a standard node
class Node:
    def __init__(self, name):
        self.incomingConnections = []
        self.nodeName = name

    def newconnection(self, incomingnode):
        self.incomingConnections.append(incomingnode)

    def debugnode(self):
        print("--- Debug of Node", self.nodeName + ":")
        print("Incoming Connections:", self.incomingConnections)
        print("--- End of Debug for Node", self.nodeName, "--- \n")



def initnodes():
    global dampeningFactor
    global nodelist

    dampeningFactor = float(input("Was ist dein 'd' Wert?"))
    print("Debug: dampeningFactor = ", dampeningFactor) if debug else None
    nodeamount = int(input("Wie viele Nodes gibt es? (>= 2 & <= 26)"))
    for i in range(nodeamount):
        nodelist.append(Node(nodeNames[i]))
    return nodelist



def initconnections(newnodes):
    for node in newnodes:
        connectionamount = int(input("Wie viele eingehende Verbindungen hat Node '" + node.nodeName + "'"))
        for j in range(connectionamount):
            node.newconnection(input(f"Von wo stammt die {j + 1}. Verbindung zu Node {node.nodeName}?"))
        if debug: node.debugnode()



if __name__ == '__main__':
    if "-debug" in sys.argv:
        debug = True
        print("Debug mode enabled")

    nodelist = initnodes()
    initconnections(nodelist)