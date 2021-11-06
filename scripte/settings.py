import os


workDir = os.getcwd()                   # legt das Arbeitsverzeichnis fest
srcFld=workDir + "/src/"                #Gibt den Ordner der Source Files an Hier liegt das File aus der BuHa
srcFldBo=srcFld + "boFile/"             #Hier liegt das File mit dem BO_Bericht
srcFile = os.listdir(srcFld)[0]         #Liest den Namen des BuHa Files
srcFileBo = os.listdir(srcFldBo)[0]     #Liest den Namen des Bo Berichtes
print("Arbeitsverzeichnis : " + workDir)


