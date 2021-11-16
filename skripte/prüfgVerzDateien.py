import os
from pathlib import Path
from colorama import init, Fore, Style # Colorama für farbige Terminalausgaben
from skripte.basis import csvSrc
init()

# Das Script prüft ob alle Verzeichnisse vorhanden sind. Ist dies nicht der Fall legt es sie an

def checkFolders(liste):
    print("Prüfung der Ordnerstruktur startet : checkFolders()")
    for pathName in liste:
        if not os.path.exists('./' + pathName):         # prüft ob Pfad nicht vorhanden ist
            print("Der Ordner : " + pathName + " Ist nicht vorhanden")    # wenn Pfad nicht vorhanden:
            os.makedirs("./" + pathName)                # erstelle das Verzeichnis
            if not os.path.exists('./' + pathName):     # prüfe nochmal auf den Verzeichnisnamen
                print("Der Ordner : " + pathName + " wurde versucht zu erstellen, hat aber nicht geklappt") # Jetzt haben wir ein Problem
            else:
                print("Der Ordner : " + pathName + " wurde korrekt erstellt")  # Gibt Erfolgsmeldung aus
        else:
            continue
    

def errorMessage():
    print(Fore.RED + "Das Script wird jetzt abgebrochen - Bitte stellen Sie die geforderten Dateien zur Verfügung")
    print(Style.RESET_ALL, end="")#Setzt die Farbeinstellungen wieder zurück
    quit()

#Dieses Script prüft ob die zum Start erforderlichen Dateien vorhanden sind
def checkFile(dir, file):
    print("Prüfung der Source Files hat begonnen : checkFile()")
    for el in file:
        myFile=""
        if el == csvSrc:
            myFile = Path(dir + "\\" + el)
            if myFile.is_file():
                #print(el + " Ist vorhanden")
                myFile=""
            else:
                print(el + " Ist nicht vorhanden und muss in das Verzeichnis kopiert werden")
                errorMessage()
        else:
            myFile=Path(el)
            if myFile.is_file():
                #print(str(myFile) + "ist vorhanden")
                continue
            else:
                print("srcFileBuHa Ist nicht vorhanden und muss in das Verzeichnis kopiert werden")
                errorMessage()   
    #print("Alle erforderlichen Dateien sind vorhanden")



