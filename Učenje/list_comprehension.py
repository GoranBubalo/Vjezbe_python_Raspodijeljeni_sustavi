#Nikad raditi na ovakav način kad je operacija jednostavna
#Klasičan
kvadrati = []
for i in range(1, 11):
    kvadrati.append(i ** 2)

print(kvadrati) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# KOristaći map + lambda
kvadrati_brojeva = list(map(lambda broj : broj **2, range(1,11)))
print(kvadrati_brojeva)

#korištenje list comprehension
kvadrati_comp = [broj ** 2 for broj in range(1, 11)]
print(kvadrati_comp)

niz = ["jabuka", "kruška", "banana", "naranča"]

#klasiča način
def lista_duljina(niz):
    duljine = []
    for string in niz:
        duljine.append(len(string))
    return duljine

print(lista_duljina(niz))

# map funkcija višeg reda
lista_duljina = list(map(lambda voce : len(voce) ,niz))
print(lista_duljina)

#List comprehension
lista_duljina_comp = [len(voce) for voce in niz]
print(lista_duljina_comp)