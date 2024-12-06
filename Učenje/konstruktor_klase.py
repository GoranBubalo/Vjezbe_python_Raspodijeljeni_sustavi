class Osoba:
    #konstruktor
    def __init__(self, ime, prezime, godine = 18):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        
    def pozdrav(self):
        return f"Pozdrv ja sam {self.ime} i imam {self.godine} godina"

osoba = Osoba("Marko", "Marić", 25)
print(osoba.ime)

osoba_2 = Osoba("Iva", "Perić", 27)
print(type(osoba_2))


osoba_3 = Osoba("Goran", "Grgin")
print(osoba_3.godine)

print(osoba_2.pozdrav())