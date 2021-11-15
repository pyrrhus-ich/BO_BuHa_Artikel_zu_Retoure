from skripte.basis import *
from skripte.prüfungen import checkFolders, checkFile
from skripte.csvFileHandling import csvToXlsx
from skripte.xlsxHandling import readSrcBuHa, bearbBOXlsx, createValList, createDstFile
from skripte.vergleichListen import vergleichListen


checkFolders(folderList);                                   #prüft ob die Folderstruktur vorhanden ist
checkFile(workDir, neededFiles)                             #prüft ob source BO und BuHa vorhanden sind
csvToXlsx(csvSrc)                                           #schreibt alle Zeilen aus dem BO csv Bericht in ein Excel File
srcFileBo = srcFldBo + os.listdir(srcFldBo)[0]              #Liest den Namen des Bo Berichtes und speichert ihn in die Variable
readSrcBuHa(srcFileBuHa)                                    #liest die Daten des BuHa Files & speichert diese in einer Liste
bearbBOXlsx(srcFileBo)                                      #Baut in der  BO xslx Datei die Retourennummer zusammen
createValList(srcFileBo)                                    #erstellt eine Liste mit den zusammengesetzten Retourennummern aus dem Bo xlsx
vergleichListen(buHaEindeutigeRetourennummer, valList)      #vergleicht beide Listen und speichert übereinstimmungen
createDstFile(resultList, dstFile)                          #Erstellt die  endgültige Datei und formatiert sie. 