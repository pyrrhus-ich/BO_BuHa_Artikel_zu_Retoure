from colorama import init, Fore, Style # Colorama für farbige Terminalausgaben
from skripte.basis import buHaEindeutigeRetourennummer, nichtGefundeneRetouren
init()

# Zähle die Anzahl der Zeilen im Buha File
# Vergleiche Anzahl der Buha Retouren mit den Retouren im dst File
# Zeige die Retouren an, die nicht gefunden wurden


def vergleichAnzahl(src, dst):  #prüft ob die Länge des src Files identisch ist mit der Länge des dst Files#
    anzZlnSrc=len(src)
    anzZlnDst=len(dst)
    if anzZlnSrc==anzZlnDst:
        print(Fore.GREEN + "Anzahl Zeilen im Basisdokument ist identisch mit dem Zieldokument")
        print(Style.RESET_ALL, end="")
    else:
        print(Fore.RED + "Die Anzahl der Zeilen differiert. Die Basisdatei enthält : " + str(anzZlnSrc) + " Das Zieldokument enthält : " + str(anzZlnDst) + " Zeilen")
        print(Style.RESET_ALL, end="")#Setzt die Farbeinstellungen wieder zurück


def checkRetoure(src):
    dst=set(src) #dst enzhält jetzt eine Liste mit allen Retourennummern die aus dem Buha File im BO File gefunden wurden
    for el in dst:
        for val in nichtGefundeneRetouren:
            if el == val:
                nichtGefundeneRetouren.remove(el)
            else:
                continue
    del nichtGefundeneRetouren[0]
    if len(nichtGefundeneRetouren)>0:
        print(Fore.RED + "Folgende Retouren wurden nicht gefunden : " + str(nichtGefundeneRetouren))
        print(Style.RESET_ALL, end="")#Setzt die Farbeinstellungen wieder zurück



