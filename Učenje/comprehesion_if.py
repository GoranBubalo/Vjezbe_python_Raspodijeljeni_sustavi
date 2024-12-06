# [expression for element in iterable if condition]
kvadrati_neparnih = []
for i in range(1, 11):
    if i % 2 != 0:
        kvadrati_neparnih.append(i ** 2)

print(kvadrati_neparnih) # [1, 9, 25, 49, 81]

# map funkcija 
kvadrati_neparnih = list(map(lambda broj : broj**2 if broj % 2 != 0 else None ,range(1,11)))
kvadrati_neparnih_filtrirano = list(filter(lambda broj: broj is not None , kvadrati_neparnih))
print(kvadrati_neparnih_filtrirano)

#list comprehension
kvadrati_neparnih_comp = [broj**2 for broj in range(1, 11) if broj % 2 != 0]
print("kvadrati_neparnih_comp",kvadrati_neparnih_comp)

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godina_rodenja": 2000},
{"ime": "Marko", "prezime": "Marković", "godina_rodenja": 1990},
{"ime": "Ana", "prezime": "Anić", "godina_rodenja": 2003},
{"ime": "Petra", "prezime": "Petrić", "godina_rodenja": 2001}
]


imena_rodenih_prije_99 = [student["ime"] for student in studenti if student["godina_rodenja"] < 1999]
print(imena_rodenih_prije_99)

#list comprehension
parni_neparni = [broj**2 if broj % 2 != 0 else broj for broj in range(1,11)]
print(parni_neparni)

#Sintaksa
# [expression1 if condition else expression2 for element in iterable]

#izvicu samo prva tri slova svakog elementa u listi 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

def prava_3(fruits):
    nova = []
    for voce in fruits:
        nova.append(voce[:3])#Slicing znaci od 0 do 3 
    return nova
print(prava_3(fruits))

# comp
#Zelimo uzeti samo voca koja sadrže slova a 
fruit_3 = [voce[:3] for voce in fruits if 'a' in voce]
print(fruit_3)


#Sto ce biti sadrzaj sljedece liste
lista_voca = ["apple", "banana", "cherry", "kiwi", "mango"]
comp_voce = [x if x != "banana" else "orange" for x in fruits]
print(comp_voce)