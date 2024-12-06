#{key_expression: value_expression for item in iterable if condition}
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#klasican nacin
duljine_voca = {}
for fruit in fruits:
    duljine_voca[fruit] = len(fruit)
    
print(duljine_voca)

#comp

duljine_voca_comp = {fruit : len(fruit) for fruit in fruits}
print(duljine_voca_comp)

bro_kvadrati = {broj : broj ** 2 for broj in range(1,6)}
print(bro_kvadrati)

def kvadriraj(x):
    return x ** 2
kvadrati_brojeva = {i: i ** 2 for i in range(1, 6)}
print(kvadrati_brojeva)

kvadrati_parnih = {broj : broj**2 for broj in range(1,11)if broj % 2 ==0}
print(kvadrati_parnih)

paran_neparan = {broj : "paran" if broj % 2 == 0 else "neparan" for broj in range(1,11)}
print(paran_neparan)