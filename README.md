# Excel
# Erstellt für Tanja Schmitt zuordnung Artikel zu Retouren
- Diese Script nimmt ein CSV File(Bo Bericht) aus dem Ordner Excel, wandelt es um in ein XSLX File und packt es nach 'src_BO
- Im Ordner src_BuHa befindet sich ein Excel File mit Markt und Retourennummer Spalte A ist Marktnummer (M199) Spalte B ist die Retourennummer
- Im dst Ordner findet sich dann das Endergebniss
- Wegen GIT sind alle Files aus den Ordnern entfernt

Vorraussetzungen:
	- Python 3 ist auf dem ausführendem Rechner installiert. 
	- Dateiendung py muss mit Python verknüpft sein
	- dst Ordner ist leer
	- src_BuHa ist leer
	- src_BO ist leer
	- Folgende Ordnerstruktur ist vorhanden (wird wenn nicht vorhanden vom Script angelegt)
    
        Excel---|
					 |-dst
					 |-src_BuHa
					 |-src_BO
					 |-scripte
                     |-log
					 |-arc
					 
					 
    - BO Bericht aus BO\Meine Favoriten\96_BuHa...\BA_BO_Bericht ist erstellt und als CSV exportiert. Dazu im Export Fenster folgendes auswählen:
		- Daten
		- Dateityp: CSV
		- Textqualifizierer: "
		- Spaltenbegrenzungszeichen: ;
		- Zeichensatz : Central European (Windows -1250)
		- Haken setzen bei: Als Standardwerte festlegen
	- Wichtig ist, das der Name nicht geändert wird.
    - Das erstellte CSV File liegt im Stammverzeichniss (Hier also 'Excel')
    - Das File der Buchhaltung ist ein Excel File mit 2 Spalten (Spalte A ist Marktnummer (M199) Spalte B ist die  Retourennummer) und liegt im Ordner src_BuHa
	
Wenn alle Vorraussetzungen erfüllt sind, sollte es funktionieren.

Wenn man aus der Konsole startet sieht man die Meldungen. Dazu Ordner in der Konsole öffnen und 
"startScript.py" eingeben. Nach Enter läuft es. Ansonsten Doppelklick auf "startScript"

Entweder in der Konsole oder im Ausgabefile werden die nichtgefundenen Retouren angezeigt. Diese dann noch
mal manuell in BO suchen und den Zeitraum des Berichtes bis zu diesem Zeitraum erweitern.

Anschliessend das Script neu starten

