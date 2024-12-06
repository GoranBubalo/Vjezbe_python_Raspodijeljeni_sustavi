#Sintaksa
# map(function, iter1, iter2)

lista = [1, 2, 3]
lista_2 = [4, 5, 6]

def zbroji(x,y):
    return x + y

rezultat = list(map(zbroji, lista, lista_2))

print(rezultat)