kontostand = 1500
zinssatz = 0.025
jahreseinzahlung = 400
laufzeit = 6 #Jahre
# Berechne für jedes Jahr:
# den neuen Kontostand nach Zinsen
# plus die jährliche Einzahlung
# Gib für jedes Jahr folgende Informationen aus:
# Jahr (1, 2, 3, …)
# aktueller Kontostand
def kontostand_beschreibung():
    if kontostand > 4000:
        return("Sehr guten Stand")
    elif kontostand > 2500 and kontostand < 4000:
        return("Soliden Stand")
    else:
        return("Niedrigen Stand ;(")

for i in range(1, 7):
    zinsen_ausrechnen = kontostand * zinssatz 
    anfang_berechnung = zinsen_ausrechnen + kontostand 
    kontostand = anfang_berechnung + jahreseinzahlung
    print(f"Neuer Kontostand nach Zinsen: {anfang_berechnung} in Jahr {i}.")
    print(f"Mit Jahreseinzahlung: {kontostand}")
    print(f"Dein Konto hat einen {kontostand_beschreibung()}")
    if i == 6:
        print(f"Kontostand am Ende der Laufzeit: {kontostand}")
    else:
        continue

input()