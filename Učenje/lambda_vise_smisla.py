def mnozi_sa_faktorom(faktor):
    return lambda x : x * faktor
#5 je x
#3 je faktor 


pomnozi_s_3 = mnozi_sa_faktorom(3)

print(pomnozi_s_3(5))