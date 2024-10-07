import json     # module to read and load the JSON file
import random   # module to shuffle list

listname = '4_Quarta_liste_prenoms.json' #path to json file

with open (listname, 'r') as f:     #read the JSON file
    names = json.load(f)

def groupes(k):               #function GROUPES with parameter k
    random.shuffle(names)               #shuffle list for randomness
    sublists = [list(set(names [i:i + k])) for i in range(0, len(names), k)]   #check for no doubles
       
    return sublists    #sublist is the the table of tables                 #return table that contains subtables (must contain k names)

k = int(input("k = ? "))

mon_tableau = groupes(k)
print(mon_tableau)



