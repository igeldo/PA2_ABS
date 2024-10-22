# PDF-Dokument-Ansatz mit Claude 3.5

In diesem Ansatz werden aus dem PDF-Dokument von Claude 3.5 Sonnet Markdown-Dokumente generiert, welche die einzelnen Kapitel beschreiben sollen.

## Vorgehen

Aufgrund einer Einschränkung an die Länge von Dokumenten wird in mehreren Schritten gearbeitet.

### Prompt 1

```plaintext
Ich habe einen Ausschnitt aus einem Leitfaden zur Diagnose und Behandlung von Infektionskrankheiten, der "2024 ABS Guide". In diesem werden die verschiedenen Diagnosekriterien und Therapiepläne in Tabellen beschrieben, häufig mit Abkürzungen. Erstelle eine ausführlichere Version als txt-Dokument. Die neue Version soll inhaltlich die gleichen Informationen übermitteln, nur das Format soll verändert werden. Füge keine neuen Informationen hinzu. Lasse keine Informationen aus. Arbeite in deutscher Sprache. Versuche, wenn möglich, alle Abkürzungen zu erklären oder auszuschreiben. Bearbeite zuerst nur das Kapitel zu CAP. Arbeite Schritt für Schritt. Im ersten Schritt beschreibe nur die Diagnostik.
```

**Anhang:**  
PDF-Version des ABS-Leitfadens

### Antwortstruktur der KI

Die Anweisung, Schritt für Schritt zu arbeiten, führt zu einer Empfehlung des nächsten Schrittes am Ende der Antworten:

```plaintext
Ich habe nun den Diagnostik-Teil für die ambulant erworbene Pneumonie (CAP) ausführlich beschrieben. Möchten Sie, dass ich mit dem nächsten Abschnitt fortfahre?
```

Die darauf folgenden Prompts hatten das Format:  
```plaintext
Ja, fahre mit der Initialtherapie fort.
```
...mit dem jeweiligen nächsten Abschnitt.

## Problem bei diesem Ansatz

Auch hier ist nicht die gesamte Information aus dem PDF abgebildet. Zum Beispiel werden logische Beziehungen wie **UND/ODER** nicht korrekt abgebildet.

### Beispiel CAP Initial - Schwere Pneumonie Standardtherapie:

- Medikament 1: Piperacillin/Tazobactam
  - Dosierung: 4 x 4,5 g täglich, intravenös
- UND
- Medikament 2: Entweder
  - Azithromycin: 1 x 500 mg täglich, oral, für 3 Tage
  - ODER
  - Clarithromycin: 2 x 500 mg täglich, oral, für 3 Tage
