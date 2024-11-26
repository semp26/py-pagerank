# py-pagerank
Eine Python Anwendung mit welcher sich der Pagrank von Webseiten iterativ berechnen lässt.

# Dateien Dokumentation
## node.py
node.py enthält die Klasse Node, welche genutzt wird, um eine "Webseite" für die Berechnung des Pageranks darzustellen.

## app.py
app.py enthält 2 Funktionen:
1. initconnections:
initconnections nimmt ein Dictionary mit IDs und ihren dazugehörigen Nodes entgegen und erstellt in einem Userdialog 
sukzessive die Verbindungen zwischen den nodes welche Verlinkungen darstellen.
Optional kann noch eine Boolean names Debug übergeben, welcher, wenn auf true gesetzt, debug Informationen zu den Nodes
ausgibt.
2. calculatepageranks:
calculatepageranks nimmt das Dictionary mit den Nodes, den dampening Faktor sowie die Anzahl der zu berechnenden 
Iterationen entgegen und berechnet die gewünschte Anzahl an Iterationen für die Pageranks aller im Dictionary
enthaltenen Nodes.