# Reaktionsspiel

## Ziel des Spieles
Entwickle ein einfaches Reaktionsspiel für zwei Spieler, die gegeneinander spielen können.
Das Spiel läuft im Browser und misst, wie schnell ein Spieler auf ein Signal reagiert.

Hinweis: Du bekommst Hilfestellungen und Code-Schnipsel

## Spielbeschreibung
- Es gibt zwei Spieler (Spieler 1 und Spieler 2)
- Das Spiel besteht aus mehreren Runden (z.B. 5)
- In jeder Runde:
  1. Spieler 1 reagiert auf das Signal
  2. Danach reagiert Spieler 2 auf das Signal
- Der schnellere Spieler gewinnt die Runde
- Der Gesamtsieger wird am Ende der Runden angezeigt

## Teilaufgaben 
## Teil A - HTML
### **Teil A1 - Datei erstellen**
Erstelle eine HTML-Datei mit: 
- head & body
- passendem Seitentitel
<br><br>

### **Teil A2 - Spielfeld anlegen**
Erstelle im Body:
- eine Überschrift mit dem Spielnamen
- einen Textbereich für den aktuellen Status
- einen Textbereich für die Runde
- einen Textbereich für den Punktestand
- einen Button zum Starten / Klicken

**Tipp**: Alle Elemente, die später von Python geändert werden, brauchen eine "id"

Beispiel (HTML und CSS):

<img width="362" height="250" alt="Bildschirmfoto 2026-01-30 um 09 12 11" src="https://github.com/user-attachments/assets/cb92086f-79bd-4557-ab98-68cd17aca33c" />
<br><br>

### **Teil A3 - PyScript einbinden**
Binde PyScript ein und lade eine externe Python-Datei (app.py)
<br><br>
<br><br>

## Teil B - CSS
### **Teil B1 - Seitenlayout**
Gestalte die Seite so, dass:
- alles zentriert ist
- Text gut lesbar ist
<br><br>


### **Teil B2 - Status & Button gestalten**
Gestalte:
- den Statusbereich auffällig
- den Button groß und klickbar
- einen deaktivierten Button optisch anders
<br><br>
<br><br>

## Teil C - Python
### **Teil C1 - Variablen**
Lege nützliche Variablen an
<br><br>

### **Teil C2 - HTML-Elemente auslesen**
Greife in Python auf:
- Button
- Statusanzeige
- Rundenzähler
- Punkteanzeige
zu und speichere sie in Variablen
**Tipp**: PyScript kann HTML-Elemente über ihre id finden.
**Hilfe:** "variabel = document.querySelector("#id")" -> findet ein HTML-Element über seine id
<br><br>

### **Teil C3 - Klick-Event**
Schreibe eine Funktion, die:
- beim Klick auf den Button aufgerufen wird
- alle weiteren Spielaktionen steuert

**Tipp:** Es wird eine "async def(event)" benötigt, damit man Wartezeiten nutzen kann
**Hilfe:** "@when("click", "#button-name")" -> Python hört auf Klicks auf den Button "#button-name"
<br><br>

### **Teil C4 - Spiel starten**
Wenn das Spiel noch nicht läuft:
- setze alle Werte zurück
- starte Runde 1
- zeige an, welcher Spieler beginnt
- zeige den Start-Spielstand an

**Hilfe:** ".innerText" -> Text, der im Browser sichtbar ist
<br><br>

### **Teil C5 - Wartephase**
Baue eine zufällige Wartezeit ein, währenddessen darf nicht geklickt werden.
Zudem gebe wichtige Daten im Browser an

**Hilfe:** "await asyncio.sleep((asyncio.get_event_loop().time() % zahl1) + zahl2)" -> erzeugt eine zufällige Wartezeit

<br><br>

### **Teil C6 - Klick erlauben**
Nach der Wartezeit:
- ändere den Status auf „JETZT KLICKEN“
- aktiviere den Button
- speichere die Startzeit
<br><br>

### **Teil C7 - Reaktionszeit messen**
Wenn das Spiel schon läuft:
Beim Klick:
- berechne die Reaktionszeit
- speichere sie für den aktuellen Spieler
- verhindere weitere Klicks

**Hilfe:** "asyncio.get_event_loop().time()" → aktuelle Zeit in Sekunden
<br><br>

### **Teil C8 - Spielerwechsel**
Wenn Spieler = 1, wechsle zu Spieler 2; sonst Runde auswerten
**Tipp:** baue dazwischen "await asyncio.sleep(1)" ein
<br><br>

### **Teil C9 - Punkte vergeben**
Vergleiche die Zeiten:
- der schnellere Spieler bekommt einen Punkt
- gebe die Punkte im Browser an
<br><br>

### **Teil C10 - Runde beenden**
Nach der Auswertung:
- Runde erhöhen
- Spieler wieder auf Spieler 1 setzen
<br><br>

### **Teil C11 - Spielende**
Wenn die maximale Rundenzahl erreicht ist:
- Spiel stoppen
- Gewinner ermitteln
- Endmeldung anzeigen
- Button wieder auf "Spiel starten" zurücksetzen












