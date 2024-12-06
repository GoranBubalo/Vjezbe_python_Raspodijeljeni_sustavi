class Student:
    def __init__(self,ime,prezime):
        self.ime = ime  
        self.prezime = prezime
    
    def pozdrav(self):
        return f"Pozdrav {self.ime} {self.prezime}!"
        
list_studenata = ["Pero", "Marko", "Saša", "Neven", "Ivan"]