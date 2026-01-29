import random
import time

# Zufallszahl zwischen 1 und 100
geheime_zahl = random.randint(1, 100)

max_versuche = 10
versuche = 0

print("🎯 Zahlenerrater")
print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")
print(f"Du hast {max_versuche} Versuche.\n")

# Startzeit speichern
startzeit = time.time()

while versuche < max_versuche:
    tipp = int(input("Gib eine Zahl ein: "))
    versuche += 1

    if tipp < geheime_zahl:
        print("⬆️ Zu niedrig!")
    elif tipp > geheime_zahl:
        print("⬇️ Zu hoch!")
    else:
        endzeit = time.time()
        benoetigte_zeit = round(endzeit - startzeit, 2)

        print("\n🎉 Richtig geraten!")
        print(f"Versuche: {versuche}")
        print(f"Zeit: {benoetigte_zeit} Sekunden")
        break
else:
    endzeit = time.time()
    benoetigte_zeit = round(endzeit - startzeit, 2)

    print("\n❌ Leider verloren!")
    print(f"Die richtige Zahl war: {geheime_zahl}")
    print(f"Zeit: {benoetigte_zeit} Sekunden")
