class Student:
    def __init__(self, ime, prezime, kolegiji):
        self.ime = ime
        self.prezime = prezime
        self.kolegiji = kolegiji
    def pozdrav(self):
        return f"Pozdrav, ja sam {self.ime} {self.prezime}."
    def ispis_kolegija(self):
        return f"Zovem se {self.ime} i moji kolegiji su: {', '.join(self.kolegiji)}."
