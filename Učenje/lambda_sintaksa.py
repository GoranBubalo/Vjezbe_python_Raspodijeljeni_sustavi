#lambda arguments: expression if condition else expression

def kvadriraj_ako_je_paran(broj):
    if broj % 2 == 0:
        return broj ** 2
    else:
        return broj

#Bolje 
kvadrat = lambda broj : broj ** 2 if broj % 2 == 0 else broj
#print(kvadrat(11))
print(kvadrat(10))

def fun (znakovni_niz):
    if len(znakovni_niz) > 5:
        return len(znakovni_niz)
    else:
        return znakovni_niz

niz = "Hello World"

print(fun(niz))

#Kako napisati lambda sto ce biti ekvivalentno funkciji
znakovni_lambda = lambda niz : len(niz)  if len(niz) > 5 else niz
print(znakovni_lambda(niz))

#Vraćaj paran string
paran_neparan = lambda broj: "paran" if broj % 2 == 0 else "neparan"
print(paran_neparan(4))