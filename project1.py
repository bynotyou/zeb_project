# Variable

kontostand = 1500.50
 
# Ausgabe


 
# Rechnen
 
# Bedingung
def kontostand_pruefen():
    if kontostand > 1000:

        return("gesund")

    else:

        return("niedrig")
 
# Schleife
def ausgabe():
    for jahr in range(1):

        kontostand_berechnet = kontostand * 1.03

        print(f"Kontostand davor: {kontostand}")
        print(f"Kontostand danach: {kontostand_berechnet}")
        print(f"Insgesamt ist dein Kontostand: {kontostand_pruefen()}")
        input()

ausgabe()