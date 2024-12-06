from faculty import studenti, operacije

marko_kolegiji = ["RJS", "WA", "RS", "MATH"]

student_marko = studenti.Student("Marko", "Marković",marko_kolegiji)

print(student_marko.ispis_kolegija())

marko_ocjene_dict = operacije.ocjene(student_marko.kolegiji)

print(marko_ocjene_dict)


marko_ocjene_rand = operacije.smuliraj_ocjene(student_marko.kolegiji)
print(marko_ocjene_rand)