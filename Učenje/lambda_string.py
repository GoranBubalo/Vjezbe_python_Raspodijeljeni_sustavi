


pozdrav = lambda ime : f"Pozdrav! {ime}"
print(pozdrav("Ivan"))

#Default vrijednost: 
pozdrav = lambda ime = "Ivan" : f"Pozdrav! {ime}"
print(pozdrav())

#Default vrijendost 
umnozak = lambda x = 10,y = 10 : x * y
print(umnozak())