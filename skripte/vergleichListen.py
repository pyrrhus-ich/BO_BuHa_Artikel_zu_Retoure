from skripte.basis import resultList

# Vergleicht die zusammengesetzten Retourennummern aus beiden Listen
def vergleichListen(srcBuHa, srcBO):
    print("Starte den Vergleich der beiden Listen" )
    for el in srcBuHa:
        for val in srcBO:
            if val[2]==el: # enthält die zusammengesetzte Retourennummer
                resultList.append(val)
    print("Der Vergleich der beiden Listen ist abgeschlossen")