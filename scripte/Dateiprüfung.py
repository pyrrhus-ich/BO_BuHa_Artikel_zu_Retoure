from genericpath import isfile
import os
from Basis import srcFileBuHa, srcFldBuHa, csvSrc, workDir
from pathlib import Path, PureWindowsPath
from tkinter import messagebox

'''
Welches ist das neueste file im Verzeichnis
'''


'''Dieses Script prüft ob die zum Start erforderlichen Dateien vorhanden sind'''

neededFiles=[csvSrc, srcFileBuHa]

def checkFile(dir, fileName):
    x = dir + "\\" + fileName
    if Path(x).exists():
        print(x + " ist vorhanden")
    else:
        print(x + " ist nicht vorhanden")
        messagebox.showwarning(title="FEHLER - Bericht ist nicht vorhanden", message=x + "\n\nist nicht vorhanden \n\n Bitte in den Ordner : \n\n" + dir + "\n\neinfügen"+
        "\n\nanschließend neu starten")
    
        

checkFile(workDir, csvSrc)



