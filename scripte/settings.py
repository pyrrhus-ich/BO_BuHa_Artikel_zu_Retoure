import os


workDir = os.getcwd()                   # legt das Arbeitsverzeichnis fest
srcFldBuHa=workDir + "/src_BuHa/"              #Gibt den Ordner der Source Files an Hier liegt das File aus der BuHa
srcFldBo = workDir + "/src_BO/"             #Hier liegt das File mit dem BO_Bericht
srcFileBuHa = srcFldBuHa + os.listdir(srcFldBuHa)[0]      #Liest den Namen des BuHa Files
srcFileBo = srcFldBo + os.listdir(srcFldBo)[0]     #Liest den Namen des Bo Berichtes

'''
#Gibt die Verzeichnisse und Dateinamen aus
print("Arbeitsverzeichnis : " + workDir + 
"\nSource Folder BO : " + srcFldBo +
"\nSource File BO : "+ srcFileBo +
"\nSource Folder Buchhaltung : " + srcFldBuHa + 
"\nSource File Buchhaltung : " + srcFileBuHa) 
'''

