import openpyxl as op
from openpyxl.worksheet.dimensions import RowDimension
from settings import *

wb = op.load_workbook(srcFile,data_only=True) # lädt das File

#print(wb.worksheets)        # Liste von Objekten
#print(wb.worksheets[0])
ws = wb.worksheets[0]
#print(ws.columns)
'''
for row in ws.values:  # Gibt alle Zeilen als Tuple aus
    print(row)

for column in ws.values:
    print(column)
'''
spalten = str(ws.max_column);
print("Anzahl der Spalten : "+ spalten)  # gibt Anzah der Spalten aus
zeilen = str(ws.max_row)
print("Anzahl der Zeilen " + zeilen)     # max. Anzahl Zeilen




