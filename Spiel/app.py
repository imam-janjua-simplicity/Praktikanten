from pyscript import when, document  # type: ignore
import asyncio

runde = 0
max_runden = 5
spieler1_punkte = 0
spieler2_punkte = 0
aktueller_spieler = 1
spieler1_zeit = 0
spieler2_zeit = 0
warte_auf_klick = False
start_zeit = 0
spiel_aktiv = False


async def spieler_zug(spieler_nummer):
    """Ein Spieler macht seinen Zug"""
    global warte_auf_klick, start_zeit, aktueller_spieler

    aktueller_spieler = spieler_nummer

    # Anzeige aktualisieren
    status = document.querySelector("#status")
    button = document.querySelector("#action-button")

    status.innerText = f"Spieler {spieler_nummer} ist dran"

    if spieler_nummer == 1:
        status.style.backgroundColor = "#2196F3"
        button.className = "action-button player1-active"
    else:
        status.style.backgroundColor = "#FF9800"
        button.className = "action-button player2-active"

    button.disabled = True
    button.innerText = "Warte..."
    status.innerText = "Warte... bereit machen!"
    status.style.backgroundColor = "orange"

    # Wartezeit basierend auf aktueller Zeit (1-4 Sekunden)
    # Nutzt die aktuelle Zeit um eine "zufällige" Wartezeit zu berechnen
    aktuelle_zeit = asyncio.get_event_loop().time()
    wartezeit = (aktuelle_zeit % 3.0) + 1.0  # Zahl zwischen 1.0 und 4.0
    await asyncio.sleep(wartezeit)

    # JETZT kann geklickt werden!
    status.innerText = "JETZT KLICKEN! 🟢"
    status.style.backgroundColor = "green"
    button.disabled = False
    button.innerText = "KLICKEN! 🟢"

    warte_auf_klick = True
    start_zeit = asyncio.get_event_loop().time()


async def neue_runde():
    """Startet eine neue Runde"""
    global runde, spieler1_zeit, spieler2_zeit

    runde += 1
    spieler1_zeit = 0
    spieler2_zeit = 0

    # Runden-Anzeige
    runden_anzeige = document.querySelector("#round-display")
    runden_anzeige.innerText = f"Runde {runde} von {max_runden}"

    # Spieler 1 beginnt
    await spieler_zug(1)


@when("click", "#action-button")
async def button_geklickt(event):
    """Button wurde geklickt - kann Spiel starten oder Reaktion messen"""
    global warte_auf_klick, spieler1_zeit, spieler2_zeit, aktueller_spieler
    global runde, spieler1_punkte, spieler2_punkte, spiel_aktiv

    # Wenn Spiel noch nicht gestartet, dann Spiel starten
    if not spiel_aktiv:
        # Spiel starten
        runde = 0
        spieler1_punkte = 0
        spieler2_punkte = 0
        spiel_aktiv = True

        score = document.querySelector("#score")
        score.innerText = "Spieler 1: 0 | Spieler 2: 0"

        await neue_runde()
        return

    # Wenn nicht auf Klick gewartet wird, ignorieren
    if not warte_auf_klick:
        return

    # Reaktionszeit berechnen
    jetzt = asyncio.get_event_loop().time()
    reaktionszeit = jetzt - start_zeit

    if aktueller_spieler == 1:
        # Spieler 1 hat geklickt
        spieler1_zeit = reaktionszeit

        status = document.querySelector("#status")
        status.innerText = f"Spieler 1: {reaktionszeit:.3f}s"
        status.style.backgroundColor = "#2196F3"

        button = document.querySelector("#action-button")
        button.disabled = True

        # Zu Spieler 2 wechseln
        asyncio.create_task(wechsel_zu_spieler2())

    else:
        # Spieler 2 hat geklickt
        spieler2_zeit = reaktionszeit

        status = document.querySelector("#status")
        status.innerText = f"Spieler 2: {reaktionszeit:.3f}s"
        status.style.backgroundColor = "#FF9800"

        button = document.querySelector("#action-button")
        button.disabled = True

        # Runde beenden
        asyncio.create_task(runde_beenden())


async def wechsel_zu_spieler2():
    """Wechselt zu Spieler 2"""
    global warte_auf_klick

    warte_auf_klick = False
    await asyncio.sleep(1)
    await spieler_zug(2)


async def runde_beenden():
    """Beendet die Runde und startet die nächste"""
    global warte_auf_klick, spieler1_punkte, spieler2_punkte, runde, spiel_aktiv

    warte_auf_klick = False

    # Gewinner der Runde bestimmen
    if spieler1_zeit < spieler2_zeit:
        spieler1_punkte += 1
    elif spieler2_zeit < spieler1_zeit:
        spieler2_punkte += 1

    # Score aktualisieren
    score = document.querySelector("#score")
    score.innerText = f"Spieler 1: {spieler1_punkte} | Spieler 2: {spieler2_punkte}"

    # Kurz warten
    await asyncio.sleep(1)

    # Nächste Runde oder Spiel beenden
    if runde < max_runden:
        await neue_runde()
    else:
        spiel_beenden()


def spiel_beenden():
    """Zeigt den Gewinner an"""
    global spiel_aktiv

    spiel_aktiv = False

    status = document.querySelector("#status")
    runden_anzeige = document.querySelector("#round-display")
    button = document.querySelector("#action-button")

    if spieler1_punkte > spieler2_punkte:
        status.innerText = (
            f"🎉 SPIELER 1 GEWINNT! ({spieler1_punkte}:{spieler2_punkte})"
        )
        status.style.backgroundColor = "#2196F3"
    elif spieler2_punkte > spieler1_punkte:
        status.innerText = (
            f"🎉 SPIELER 2 GEWINNT! ({spieler1_punkte}:{spieler2_punkte})"
        )
        status.style.backgroundColor = "#FF9800"
    else:
        status.innerText = f"🤝 UNENTSCHIEDEN! ({spieler1_punkte}:{spieler2_punkte})"
        status.style.backgroundColor = "purple"

    runden_anzeige.innerText = "Spiel beendet!"
    button.disabled = False
    button.innerText = "Spiel starten"
    button.className = "action-button"
