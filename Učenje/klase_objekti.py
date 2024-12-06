#Ovo nema puno smisla zato sto smo hard codirali 
class Osoba:
    ime = "Ivan"
    prezime = "Ivić"
    godine = 25

Osoba = Osoba() # ---->  pozivamo lasu kao i funkcija 
print(Osoba.ime)

osoba_2 = Osoba()

print(osoba_2.ime)