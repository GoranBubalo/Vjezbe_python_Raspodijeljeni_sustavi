class Korisnik:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
        self.username = f"{ime.lower()}_{prezime.lower()}"

    def pozdrav(self):
        return f"Pozdrav, ja sam {self.ime} {self.prezime}, moj username je {self.username}."

korisnik = Korisnik("Luka","Lukič")
print(korisnik.username)

class Admin(Korisnik): #Nova klasa koja nasljeđje korisnika 
    def __init__(self, ime, prezime, privilegije): #konstruktor koji nasljeđuje 
        #Atribute is super klase 
        super().__init__(ime, prezime) #nasljeđujemo atribute od nadklase
        self.privilegije = privilegije
        def pozdrav(self):
            return f"Pozdrav, ja sam {self.ime} {self.prezime}, moj username je {self.username}. Imam privilegije:  {', '.join(self.privilegije)} "
        

privilegije = {"dodavanje korisnika", "brisanje korisnika", "ažuiranje korisnika"}

admin_user = Admin("Pero","Perić", privilegije)


print(admin_user.pozdrav())