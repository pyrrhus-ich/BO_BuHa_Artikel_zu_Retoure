import openpyxl as op
from settings import *

wb = op.load_workbook(srcFile)
ws = wb['Tabelle1']
value = ws["B15"].value
print(value)
print(wb.sheetnames)



