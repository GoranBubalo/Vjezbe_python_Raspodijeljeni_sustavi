from greetings import list_studenata, Student
from math_operations import zbroj, oduzimanje
#Importaj sve
from math_operations import *  # ili ovako
import math_operations as mp #ali onda moraš naglašavati 

#print(greetings.pozdrav("Goran"))

student = Student("Ana","Anić")#
print(student.pozdrav())

print(list_studenata)

print(zbroj(5,6))