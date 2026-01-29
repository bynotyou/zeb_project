import os

class bizhar():
    def __init__(self, measure):
        self.measure = measure

class dreieck(bizhar):
    def __init__(self, measure):
        super().__init__(measure) 
    def rechnung(self):
        rechnung = 0.5 * self.measure[0] * self.measure[1]
        return rechnung

class quadrat(bizhar):
    def __init__(self, measure):
        super().__init__(measure)
    def rechnung(self):
        rechnung = self.measure[0] * self.measure[1]
        return rechnung
    
class kreis(bizhar):
    def __init__(self, r):
        super().__init__(r)
    def rechnung(self):
        rechnung = 3.14159 * self.measure**2
        return rechnung

def bizhar_checker(inp) -> bool:
    inp = inp.lower()
    valid_inputs = ["1", "2", "3"]
    if inp in valid_inputs:
        return True
    else: 
        return False

def e():
    print("Falscher Input. Bitte gebe 1, 2 oder 3 ein.")
    input()
    exit()

def eingabsteuerung():
    inp = input("Was möchtest du berechnen? \n1 = Dreieck \n2 = Quadrat \n3 = Kreis\n")
    if bizhar_checker(inp):
        pass
    else: 
        e()

    if inp == "3":
        r = float(input("Dein r: "))
        print("Kreis: ", kreis(r).rechnung())
    elif inp == "2":
        a = float(input("Dein a: "))
        b = float(input("Dein b: "))
        print("Quadrat: ", quadrat([a, b]).rechnung())
    elif inp == "1":
        a = float(input("Dein a: "))
        b = float(input("Dein b: "))
        print("Dreieck: ", dreieck([a, b]).rechnung())

eingabsteuerung()