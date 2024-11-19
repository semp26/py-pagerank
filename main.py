import sys


nodeNames = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nodelist = []


# definition of a standard node
class Node:
    def __init__(self, name):
        self.incomingConnections = []
        self.nodeName = name

    def newconnection(self, incomingnode):
        self.incomingConnections.append(incomingnode)

    def debugnode(self):
        print("Debug of Node ", self.nodeName, ":")
        print(self.incomingConnections)
        print("--- End of Debug for Node ", self.nodeName, " ---")



def initnodes():
    global dampeningFactor
    dampeningFactor = float(input("Was ist dein 'd' Wert?"))
    print("Debug: dampeningFactor = ", dampeningFactor) if debug else None
    nodeAmount = int(input("Wie viele Nodes gibt es? (>= 2 & <= 26)"))

    for i in range(nodeAmount):
        nodelist.append(Node(nodeNames[i]))

    for node in nodelist:
        node.debugnode()



if __name__ == '__main__':
    if "-debug" in sys.argv:
        debug = True
        print("Debug mode enabled")

    initnodes()