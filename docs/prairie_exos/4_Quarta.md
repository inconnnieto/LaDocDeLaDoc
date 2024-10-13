# 4_Quarta

## brief:
Task: create random groups of learners from list of names of class.

Goal: write a function that splits list of names into smaller groups

## my attempt:

Input: list of names stored in .json file

Output: list of groups, each containing `k` names, no duplicates

## steps
Pseudo code:
* create list of names and save in .json format
* load list of names
* create function `groupes` taking parameter `k` (n of learners in group)
* randomly shuffle names
* split shuffled into groups


```json
[
    "Chaymae",
    "Connie",
    "Manal",
    "Mariam",
    "Harold",
    "Colas",
    "Mathieu",
    "Mattias",
    "Bruno",
    "Léo",
    "Karolan",
    "Sofian",
    "Avriska",
    "Ioana"
]
```

## Python implementation


``` py
import json     # module to read and load the JSON file
import random   # module to shuffle list

listname = '4_Exo_Quarta.json' #path to json file

with open (listname, 'r') as f:     #read the JSON file
    names = json.load(f)

def groupes(k):               #function GROUPES with parameter k
    random.shuffle(names)               #shuffle list for randomness
    sublists = [list(set(names [i:i + k])) for i in range(0, len(names), k)]   #check for no doubles
    return sublists    #sublist is the the table of tables                 #return table that contains subtables (must contain k names)

k = int(input("how much is k = ? "))

mon_tableau = groupes(k)
print(mon_tableau)
```


## JS implementation

``` javascript
import namelist from './4_Exo_Quarta.json' assert {type: 'json'};

function groupes(k) {
    if (k < 1) { throw new Error("nope"); }
    let l = [...namelist];
    l.sort((a, b) => Math.random() - 0.5);
    let result = [];
    while (l.length > 0) {
        result.push(l.splice(0, k));
    }
    return result;
}

const k = 4;
console.log(groupes(k));
```

## notes
Edge case:
problem / situation arises when program encounters inputs/ conditions at the `limits` of its expected operational range

in this exo
* Empty list name
* Group size larger than list length
* Uneven division of groups - last group contain fewer members if necessary