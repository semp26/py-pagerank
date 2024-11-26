def initconnections(newnodes, debug = False):
    mappingdict = {}
    for nodeid, node in newnodes.items():
        mappingdict[node.nodeName] = nodeid

    for node in newnodes.values():
        connectionamount = int(
            input(f"Wie viele eingehende Verbindungen hat Node '{node.nodeName}'?")
        )
        for j in range(connectionamount):
            node.newconnection(mappingdict.get(
                input(f"Von wo stammt die {j + 1}. Verbindung zu Node {node.nodeName}?")
            ))
        if debug: node.debugnode()

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
