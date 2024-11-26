import sys
from node import Node
from app import initconnections, calculatepageranks


def initnodes(nodedict):
    init_dampeningfactor = float(input("Was ist dein 'd' Wert?"))

    nodeamount = int(input("Wie viele Nodes gibt es? (>= 2 & <= 26)"))
    initialvalue = int(input("Was soll der Startwert der Pageranks sein?"))
    for i in range(nodeamount):
        nametmp = str(input(
            f"Wie soll die {i+1}. Node heißen? (Node Namen dürfen nicht doppelt sein)"
        ))
        nodetemp = Node(nametmp, initialvalue)
        nodedict[id(nodetemp)] = nodetemp
    return nodedict, init_dampeningfactor


def parseargs(arguments):
    defaults = "-defaults" in arguments
    debug = "-debug" in arguments
    return defaults, debug


def runwithdefaults():
    nodedict =  {}
    print("Default values enabled")
    tmphold1 = Node("FA", 0)
    nodedict[id(tmphold1)] = tmphold1
    tmphold2 = Node("FB", 0)
    nodedict[id(tmphold2)] = tmphold2
    tmphold3 = Node("FC", 0)
    nodedict[id(tmphold3)] = tmphold3
    dampeningfactor = 0.85
    tocalc = 15
    tmphold1.newconnection(id(tmphold2))
    tmphold2.newconnection(id(tmphold1))
    tmphold3.newconnection(id(tmphold1))
    tmphold3.newconnection(id(tmphold2))
    for defaults_j in nodedict.values():
        for incomingcons in defaults_j.incomingConnections:
            nodedict.get(incomingcons).outgoingConnections.append(incomingcons)
    nodedict = calculatepageranks(tocalc, nodedict, dampeningfactor)

    print(tocalc)
    for nodeval in nodedict.values():
        print(f"{nodeval.nodeName}: {nodeval.ranking}")


def runnormal(debug):
    nodedict = {}
    debugmode = debug
    nodedict, dampeningfactor = initnodes(nodedict)
    nodedict = initconnections(nodedict, debugmode)

    tocalc = int(input("Wie oft soll der Pagerank der Seiten iterativ berechnet werden?: "))
    nodedict = calculatepageranks(tocalc, nodedict, dampeningfactor)

    print(tocalc)
    for nodeval in nodedict.values():
        print(f"{nodeval.nodeName}: {nodeval.ranking}")


if __name__ == '__main__':
    DEFAULTS, DEBUG = parseargs(sys.argv)

    if DEFAULTS:
        runwithdefaults()
    else:
        runnormal(DEBUG)