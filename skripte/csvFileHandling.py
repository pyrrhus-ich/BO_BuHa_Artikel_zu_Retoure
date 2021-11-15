import os, csv
import openpyxl as op
from basis import *


#<<<<<<< Hier wird das CSV File in ein XLSX File umgewandelt >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def csvToXlsx(sourceFile):
    print("csv wird in Excel umgewandelt")
    csvWb = op.Workbook()
    csvWs = csvWb.active
    with open(sourceFile) as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            csvWs.append(row)
    csvWb.save(srcFldBo + 'BA_BO_Bericht.xlsx')
    f.close()
    print("Excel File wurde erstellt in : " + srcFldBo)


                
        
        
        




        







