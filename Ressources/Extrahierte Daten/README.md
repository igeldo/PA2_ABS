# Dokumentenextraktion mit Claude

Wenn bei Claude ein PDF-Dokument als Kontext hochgeladen wird, wird es als extrahiertes Text-Dokument verwendet.  
Das Resultat ist in der Datei **ABS-PDF-Default-Extraction.txt** zu sehen.

## Problem: Verlust der Strukturinformationen

Die Informationen aus der Struktur des Dokumentes, in diesem Fall vor allem die **Tabellenstruktur**, gehen hierbei verloren.

## Lösungsansatz

Um dies zu beheben, werden in den Unterverzeichnissen verschiedene Ansätze getestet.


## Weitere Probleme 

Der Leitfaden selbst ist an verschiedenen Stellen ungenau formuliert:

- Nicht alle Therapien haben eine Zeitdauer
- Probleme mit und/oder:
  - "Ceftriaxon 1 x 2 g i.v. und Azithromycin 1 x 500 mg p.o. oder Clarithromycin 2x500 mg p.o. für 7 Tage"
  - Option 1: "(A AND B) OR C" , Option 2 "A AND (B OR C)"