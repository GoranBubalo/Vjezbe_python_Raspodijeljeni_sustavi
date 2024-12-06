tekst = "Ovo je neki tekst"


#veliki_tekst = lambda tekst: tekst.upper()
#print(veliki_tekst(tekst))

#drugi način - nije poželjno raditi
print((lambda tekst: tekst.upper())(tekst))