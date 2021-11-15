from skripte.basis import *
from skripte.prüfungen import checkFolders, checkFile
from skripte.csvFileHandling import csvToXlsx
from skripte.xlsxHandling import readSrcBuHa, bearbBOXlsx, createValList, createDstFile
from skripte.vergleichListen import vergleichListen


checkFolders(folderList); #von prüfungen.py prüft ob die Folderstruktur vorhanden ist
checkFile(workDir, neededFiles) #von prüfungen.py prüft ob source BO und BuHa vorhanden sind
csvToXlsx(csvSrc) #Kommt von csvHandling und schreibt alle Zeilen aus dem BO csv Bericht in ein Excel File
srcFileBo = srcFldBo + os.listdir(srcFldBo)[0]  #Liest den Namen des Bo Berichtes und speichert ihn in die Variable
readSrcBuHa(srcFileBuHa) #Kommt von xlsxHandling, liest die Daten des BuHa Files & speichert diese in einer Liste
bearbBOXlsx(srcFileBo)#von xlsxHandling.py Baut im BO File die Retourennummer zusammen
createValList(srcFileBo)#von xlsx Handling erstellt eine Liste mit den zusammengesetzten Retourennummern aus dem Bo xlsx
vergleichListen(buHaEindeutigeRetourennummer, valList)#xslxHandling.py vergleicht beide Listen und speichert übereinstimmungen
createDstFile(resultList, dstFile)