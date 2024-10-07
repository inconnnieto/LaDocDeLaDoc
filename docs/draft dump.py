import json
import random

listname = '4_Quarta_liste_prenoms.json'

with open(listname, 'r') as j:
        l = json.load(j)

def groupe(k):
    if k < 1: raise ValueError("NAN")
    data = l.copy()
    random.shuffle(data)
    result = []
    while len(data) > 0:
        g = []
        for i in range(k):
            g.append(data.pop())
            if len(data) == 0: break
        result.append(g)
    return result