#filter(function, iterables)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filtriraj_parne(lista):
    parni = []
    for element in lista:
        if element % 2 == 0:
            parni.append(element)
    return parni


#Bolji nacin pisanja pomocu filtera
parni = list(filter(lambda broj : broj % 2 == 0 ,lista))
print(parni)

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "jmbag": "0303077889", "godina_rodenja" : 2000},
{"ime": "Marko", "prezime": "Marković", "jmbag": "0303099878", "godina_rodenja" :
1999},
{"ime": "Ana", "prezime": "Anić", "jmbag": "0303088777", "godina_rodenja" : 2003},
{"ime": "Petra", "prezime": "Petrić", "jmbag": "0303088777", "godina_rodenja" : 2001}
]

rodeni_prije_2000 = list(filter(lambda student: student["godina_rodenja"] < 2000 ,studenti))
print(rodeni_prije_2000)