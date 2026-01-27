transaktionen = [1200, -200, -450, 300, -150, -800, 500, -50]
transaktionen_positiv = []
transaktionen_negativ = []

#Hinweis (Geldeingang ist positiver Wert, Geldausgang ist negativer Wert)

def zahlen():
    anzahl_transaktionen = len(transaktionen)
    gesammtsaldo = sum(transaktionen)
    for transaktion in transaktionen:
        try:
            float(transaktion)
            if transaktion < 0:
                pass
            else:
                transaktionen_positiv.append(transaktion)
        except Exception as e:
            print(f"Eintrag in der Liste ist keine Zahl. Error Code: {e}")
    for transaktion in transaktionen:
        try:
            float(transaktion)
            if transaktion > 0:
                pass
            else:
                transaktionen_negativ.append(transaktion)
        except Exception as e:
            print(f"Eintrag in der Liste ist keine Zahl. Error Code: {e}")
    liste_positiv = len(transaktionen_positiv)
    liste_negativ = len(transaktionen_negativ)
    float(liste_positiv)
    float(liste_negativ)
    print("---------------------Warnungen---------------------")
    if gesammtsaldo < 0:
        konto_information = "Warnung: Konto im Minus"
    if liste_positiv < liste_negativ:
        print("Achtung: Viele Ausgaben")
    for i in transaktionen_negativ:
        if i < -500:
            print("Große Einzelbelastung erkannt")
        else:
            pass
    print("--------------------Informationen--------------------")
    print(f"Anzahl der Transaktionen: {anzahl_transaktionen}")
    print(f"Gesammtsaldo: {gesammtsaldo}")
    print(f"Summe aller Einträge: {liste_positiv}")
    print(f"Summe aller Ausgänge: {liste_negativ}")
    print("-----------------------------------------------------")
    input()

zahlen()
