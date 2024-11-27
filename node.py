class Node:
    def __init__(self, nodename, startvalue):
        self.incomingConnections = []
        self.outgoingConnections = []
        self.nodeName = nodename
        self.ranking = []
        self.ranking.append(startvalue)

    def newconnection(self, incomingnode):
        # Die ID der Node, von welcher die eingehende Verbindung ausgeht wird in die Liste angefügt
        self.incomingConnections.append(int(incomingnode))

    def debugnode(self):
        print("--- Debug of Node", self.nodeName, ":")
        print("Incoming Connections:", self.incomingConnections)
        print("Rankings:", self.ranking)
        print("--- End of Debug for Node", self.nodeName, "--- \n")
