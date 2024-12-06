brojevi = [4, 7, 1, 2, 4, 7, 9, 10]
brojevi_2 = [6, 8, 10, 14,13]

def svi_parni(lista):
    for element in lista:
        if element % 2 !=0:
            return False
    return True



#Ovu funkciju ćemo definirati pomocu novih funkcija
#Sintaksa
# any(iteratibilni_element), #all(iterabilni_element)
# [True, False, False, True]

print(any(list(map(lambda broj: broj % 2 == 0 ,brojevi_2))))

putnici = [
{"ime": "Ivan", "prezime": "Ivić", "uplata": True},
{"ime": "Marko", "prezime": "Marković", "uplata": True},
{"ime": "Ana", "prezime": "Anić", "uplata": False}
]

svi_uplatili = all(list(map(lambda putnik : putnik["uplata"],putnici)))
print(svi_uplatili)