import os
from Basis import folderList

'''
Das Script prüft ob alle Verzeichnisse vorhanden sind. Ist dies nicht der Fall legt es sie an
'''
def checkFolders(liste):
    for pathName in liste:
        if not os.path.exists('./' + pathName):         # prüft ob Pfad nicht vorhanden ist
            print(pathName + " Ist nicht vorhanden")    # wenn Pfad nicht vorhanden:
            os.makedirs("./" + pathName)                # erstelle das Verzeichnis
            if not os.path.exists('./' + pathName):     # prüfe nochmal auf den Verzeichnisnamen
                print(pathName + " wurde versucht zu erstellen, hat aber nicht geklappt") # Jetzt haben wir ein Problem
            else:
                print(pathName + " wurde korrekt erstellt")  # Gibt Erfolgsmeldung aus
        else:
            print(pathName + " ist bereits vorhanden") # Meldung falls Pfad bereits vorhanden ist
    print("Alle Pfade sind da, Es kann los gehen")  # Schlussmeldung


