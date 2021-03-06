import os
from datetime import datetime as dt
#Diese Datei legt die Basisvariablen fest. Z.B. Die Namen für die  Ordnerstruktur

workDir = os.getcwd()                                   # legt das Arbeitsverzeichnis fest
folderList = ["dst", "src_BuHa", "src_BO", "log", "arc"]              # legt die Liste der Verzeichnisse fest
csvSrc = "BA_BO_Bericht.csv"                            # Gibt das source CSV File an
srcFldBuHa=workDir + "\\src_BuHa\\"                       #Gibt den Ordner der Source Files an. Hier liegt das File aus der BuHa
srcFldBo = workDir + "/src_BO/"                         #Hier liegt das File mit dem BO_Bericht
srcFileBuHa = srcFldBuHa + os.listdir(srcFldBuHa)[0]  if len(os.listdir(srcFldBuHa))>0 else ""  #Liest den Namen des BuHa Files
#srcFileBuHa=''                                          # wird erst mal nur deklariert
srcFileBo =''                                           # wird erst mal nur deklariert
# legt dateTime fest damit jede datei unique benamst werden kann
now = dt.now()
dateTime = now.strftime("%Y%m%d-%H%M%S")
#Hier werden der Pfad und der Filename des Zielfiles angegeben
dstFileName=dateTime + "-" + "Zuordnung_Artikel_zur_Retoure.xlsx"
dstFile='./dst/'+dstFileName
neededFiles=[csvSrc, srcFileBuHa]        # List der für den Start erforderlichen Dateien
buHaValList=[];                          # enthält die Liste aus der BuHa Basisdatei 
buHaEindeutigeRetourennummer =[]         # zusammengesetzte Retourennummer aus dem Src File der Buchhaltung
valList=[]                               # zusammengesetzte Retourennummer aus dem SrcFile BO xlsx
resultList=[("BuKr","Retoure","Zusammengesetzt","Artikelnummer","Artikelbezeichnung", "Abt.-ID", "Abteilung")]; #speichert die Listeneinträge aus valList die auch in BuHaEindeutige Retourennummer vorkommen
resLstRetNr=[] #enthält alle Zeilen der Retourennummern also für jeden Artikel eine Zeile
nichtGefundeneRetouren=buHaEindeutigeRetourennummer