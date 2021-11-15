# Excel

- Diese Script nimmt ein CSV File(Bo Bericht) aus dem Ordner Excel, wandelt es um in ein XSLX File und packt es nach 'src_BO
- Im Ordner src_BuHa befindet sich ein Excel File mit Markt und Retourennummer Spalte A ist Marktnummer (M199) Spalte B ist die Retourennummer
- Im dst Ordner findet sich dann das Endergebniss
- Wegen GIT sind alle Files aus den Ordnern entfernt
Vorraussetzungen:
    Ordnerstruktur:
        Excel---|
                |-dst
                |-src_BuHa
                |-src_BO
                |-scripte
                |-log
                |-arc
    1. BO Bericht aus BO\Meine Favoriten\96_BuHa...\BA_BO_Bericht ist erstellt und als CSV exportiert
    2. Das erstellte CSV File liegt im Stammverzeichniss (Hier also 'Excel')
    3. Das File der Buchhaltung ist ein Excel File mit 2 Spalten (Spalte A ist Marktnummer (M199) Spalte B ist die Retourennummer)
Wenn alle Vorraussetzungen erfüllt sind, sollte es funktionieren.
