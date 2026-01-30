from pyscript import when, document
import asyncio

# --- Spielzustand ---
runde = 0
max_runden = 5
punkte = [0, 0]       # Spieler 1 = Index 0, Spieler 2 = Index 1
zeiten = [0, 0]
aktueller_spieler = 1  # Startspieler = 1
warte_auf_klick = False
start_zeit = 0
spiel_aktiv = False

button_el = document.querySelector("#action-button")
status_el = document.querySelector("#status")
score_el = document.querySelector("#score")
round_el = document.querySelector("#round-display")

@when("click", "#action-button")
async def button(event):
    global spiel_aktiv, runde, aktueller_spieler, warte_auf_klick, start_zeit


    if not spiel_aktiv:
        # Neues Spiel starten
        spiel_aktiv = True
        runde = 0
        punkte[:] = [0, 0]
        score_el.innerText = "Spieler 1: 0 | Spieler 2: 0"
    else:
        if warte_auf_klick:
            # Reaktionszeit speichern
            zeiten[aktueller_spieler-1] = asyncio.get_event_loop().time() - start_zeit
            status_el.innerText = f"Spieler {aktueller_spieler}: {zeiten[aktueller_spieler-1]:.3f}s"
            button_el.disabled = True

            if aktueller_spieler == 1:
                # Spieler 2 ist dran
                await asyncio.sleep(1)
                aktueller_spieler = 2
            else:
                # Runde auswerten
                if zeiten[0] < zeiten[1]:
                    punkte[0] += 1
                elif zeiten[1] < zeiten[0]:
                    punkte[1] += 1
                score_el.innerText = f"Spieler 1: {punkte[0]} | Spieler 2: {punkte[1]}"
                await asyncio.sleep(1)
                runde += 1
                if runde >= max_runden:
                    # Spielende
                    spiel_aktiv = False
                    if punkte[0] > punkte[1]:
                        status_el.innerText = f"🎉 Spieler 1 gewinnt ({punkte[0]}:{punkte[1]})"
                    elif punkte[1] > punkte[0]:
                        status_el.innerText = f"🎉 Spieler 2 gewinnt ({punkte[0]}:{punkte[1]})"
                    else:
                        status_el.innerText = f"🤝 Unentschieden ({punkte[0]}:{punkte[1]})"
                    button_el.innerText = "Spiel starten"
                    button_el.disabled = False
                    round_el.innerText = "Spiel beendet!"
                    return
                aktueller_spieler = 1  # Nächste Runde startet mit Spieler 1

    # Nächster Zug vorbereiten
    warte_auf_klick = False
    round_el.innerText = f"Runde {runde+1} von {max_runden}"
    status_el.innerText = f"Spieler {aktueller_spieler} bereit..."
    button_el.innerText = "Warte..."
    button_el.disabled = True

    # Zufällige Wartezeit 1–4 Sekunden
    await asyncio.sleep((asyncio.get_event_loop().time() % 3) + 1)

    # Jetzt kann der Spieler klicken
    status_el.innerText = "JETZT KLICKEN! 🟢"
    button_el.innerText = "KLICKEN! 🟢"
    button_el.disabled = False
    warte_auf_klick = True
    start_zeit = asyncio.get_event_loop().time()
