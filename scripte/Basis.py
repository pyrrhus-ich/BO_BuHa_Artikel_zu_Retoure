'''
Das Script legt die Basisvariablen fest. Z.B. Die Namen für die  Ordnerstruktur
'''
import os

workDir = os.getcwd()                                   # legt das Arbeitsverzeichnis fest

folderList = ["dst", "src_BuHa", "src_BO", "log"]              # legt die Liste der Verzeichnisse fest



csvSrc = "BA_BO_Bericht.csv"                            # Gibt das source CSV File an
srcFldBuHa=workDir + "\\src_BuHa\\"                       #Gibt den Ordner der Source Files an. Hier liegt das File aus der BuHa
srcFldBo = workDir + "/src_BO/"                         #Hier liegt das File mit dem BO_Bericht
srcFileBuHa = srcFldBuHa + os.listdir(srcFldBuHa)[0]  if len(os.listdir(srcFldBuHa))>0 else ""  #Liest den Namen des BuHa Files
#srcFileBuHa=''                                          # wird erst mal nur deklariert
srcFileBo =''                                           # wird erst mal nur deklariert
#Hier werden der Pfad und der Filename des Zielfiles angegeben
dstFileName="Zuordnung_Artikel_zur_Retoure.xlsx"
dstFile='./dst/'+dstFileName

print(srcFileBuHa)
