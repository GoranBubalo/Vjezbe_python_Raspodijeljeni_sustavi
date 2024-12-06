import random

def ocjene(kolegiji):
    return {kolegij: [] for kolegij in kolegiji}

def smuliraj_ocjene(koelegij):
    return {koelegij : [random.randint(1,5) for _ in range (5)] for koelegij in koelegij}