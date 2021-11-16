from skripte.basis import *
from skripte.prüfgVerzDateien import checkFolders, checkFile
from skripte.prfgInhaltDatei import checkRetoure, vergleichAnzahl
from skripte.csvFileHandling import csvToXlsx
from skripte.xlsxHandling import readSrcBuHa, bearbBOXlsx, createValList, createDstFile
from skripte.vergleichListen import vergleichListen


checkFolders(folderList);                                   #prüft ob die Ordnerstruktur vorhanden ist
checkFile(workDir, neededFiles)                             #prüft ob die Startdateien BA_BO_Berichte.csv und die Datei der BuHa vorhanden sind
csvToXlsx(csvSrc)                                           #schreibt alle Zeilen aus dem BA_BO_Berichte.csv in eine Excel Datei
srcFileBo = srcFldBo + os.listdir(srcFldBo)[0]              #Liest den Namen des Bo Berichtes und speichert ihn in die Variable
readSrcBuHa(srcFileBuHa)                                    #liest die Daten der BuHa Datei & speichert diese in einer Liste
vergleichAnzahl(buHaValList,buHaEindeutigeRetourennummer)   
bearbBOXlsx(srcFileBo)                                      #Baut in der  BO xslx Datei die Retourennummer zusammen
createValList(srcFileBo)                                    #erstellt eine Liste mit den zusammengesetzten Retourennummern aus dem Bo xlsx
vergleichListen(buHaEindeutigeRetourennummer, valList)      #vergleicht beide Listen und speichert übereinstimmungen
checkRetoure(resLstRetNr)
createDstFile(resultList, dstFile)                          #Erstellt die  endgültige Datei und formatiert sie. 

