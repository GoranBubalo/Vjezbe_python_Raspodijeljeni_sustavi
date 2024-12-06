def primijeni_na_sve(lista, funkcija):
    

    
    rezultat = []
    for element in lista:
        rezultat.append(funkcija(element)) # u novu listu dodajemo rezultate funkcije primijenjene na svaki element
    return rezultat

brojevi = [1, 2, 3, 4, 5]


na_potenciju = primijeni_na_sve(brojevi, lambda n : n **2)
print(na_potenciju)

uvecani = primijeni_na_sve(brojevi, lambda n: n +5)
print(uvecani)