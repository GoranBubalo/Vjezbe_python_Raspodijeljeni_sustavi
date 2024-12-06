# map(function, iterables)
lista = [1,2,3,4]
lista_2 = list(map(lambda x : x**2, lista))
print(lista_2)

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "jmbag": "0303077889"},
{"ime": "Marko", "prezime": "Marković", "jmbag": "0303099878"},
{"ime": "Ana", "prezime": "Anić", "jmbag": "0303088777"}
]

def izvuci_jmbagove(studenti):
    jmbagovi = []
    
    for student in studenti:
        jmbagovi.append(student["jmbag"])
    return jmbagovi

print(izvuci_jmbagove(studenti))

#Riješenje pomoću lambade
jmbagovi = list(map(lambda student : student["jmbag"] ,studenti))
print("jmbagovi", jmbagovi)