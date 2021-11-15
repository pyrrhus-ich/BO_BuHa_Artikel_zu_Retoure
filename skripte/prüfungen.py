import os
from pathlib import Path

from basis import *


# Das Script prüft ob alle Verzeichnisse vorhanden sind. Ist dies nicht der Fall legt es sie an

def checkFolders(liste):
    print("Prüfung der Ordnerstruktur startet")
    for pathName in liste:
        if not os.path.exists('./' + pathName):         # prüft ob Pfad nicht vorhanden ist
            print("Der Ordner : " + pathName + " Ist nicht vorhanden")    # wenn Pfad nicht vorhanden:
            os.makedirs("./" + pathName)                # erstelle das Verzeichnis
            if not os.path.exists('./' + pathName):     # prüfe nochmal auf den Verzeichnisnamen
                print("Der Ordner : " + pathName + " wurde versucht zu erstellen, hat aber nicht geklappt") # Jetzt haben wir ein Problem
            else:
                print("Der Ordner : " + pathName + " wurde korrekt erstellt")  # Gibt Erfolgsmeldung aus
        else:
            print("Der Ordner : " + pathName + " ist bereits vorhanden") # Meldung falls Pfad bereits vorhanden ist
    print("Prüfung der Ordnerstruktur ist beendet")# Schlussmeldung

def errorMessage():
    print("Das Script wird jetzt abgebrochen - Bitte stellen Sie die geforderten Dateien zur Verfügung")
    quit()

#Dieses Script prüft ob die zum Start erforderlichen Dateien vorhanden sind
def checkFile(dir, file):
    print("\nPrüfung der Source Files hat begonnen")
    for el in file:
        myFile=""
        if el == csvSrc:
            myFile = Path(dir + "\\" + el)
            if myFile.is_file():
                print(el + " Ist vorhanden")
                
                myFile=""
            else:
                print(el + " Ist nicht vorhanden und muss in das Verzeichnis kopiert werden")
                errorMessage()
        else:
            myFile=Path(el)
            if myFile.is_file():
                print(str(myFile) + "ist vorhanden")
            else:
                print("srcFileBuHa Ist nicht vorhanden und muss in das Verzeichnis kopiert werden")
                errorMessage()   
    print("Alle erforderlichen Dateien sind vorhanden - Es kann los gehen\n")

# Zähle die Anzahl der Zeilen im Buha File

# Vergleiche Anzahl der Buha Retouren mit den Retouren im dst File

# Zeige die Retouren an, die nicht gefunden wurden

