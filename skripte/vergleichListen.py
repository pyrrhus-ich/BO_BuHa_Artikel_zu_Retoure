from skripte.basis import resultList, resLstRetNr

# Vergleicht die zusammengesetzten Retourennummern aus beiden Listen und hängt die Werte an die Resultlist
def vergleichListen(srcBuHa, srcBO):
    print("Starte den Vergleich der beiden Listen : vergleichListen()" )
    for el in srcBuHa:
        for val in srcBO:
            if val[2]==el: # enthält die zusammengesetzte Retourennummer
                resultList.append(val)
                resLstRetNr.append(val[2])
    #print("Der Vergleich der beiden Listen ist abgeschlossen, Variablen 'resultList' und 'resLstRetNr' ist mit Daten befüllt")



