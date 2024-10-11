# 7_Septima 
## python algo trinker

```python
import json
from pprint import pprint
from termcolor import colored
import math

with open('people.json', 'r', encoding='utf-8') as p:
    people = json.loads(p.read())

print(colored("""
$$$$$$$$\\        $$\\           $$\\                           $$\\                               
\\__$$  __|       \\__|          $$ |                          $$ |                              
   $$ | $$$$$$\\  $$\\ $$$$$$$\\  $$ |  $$\\  $$$$$$\\   $$$$$$\\  $$ | $$$$$$\\ $$\\    $$\\  $$$$$$\\  
   $$ |$$  __$$\\ $$ |$$  __$$\\ $$ | $$  |$$  __$$\\ $$  __$$\\ $$ |$$  __$$\\\\$$\\  $$  |$$  __$$\\ 
   $$ |$$ |  \\__|$$ |$$ |  $$ |$$$$$$  / $$$$$$$$ |$$ |  \\__|$$ |$$ /  $$ |\\$$\\$$  / $$$$$$$$ |
   $$ |$$ |      $$ |$$ |  $$ |$$  _$$<  $$   ____|$$ |      $$ |$$ |  $$ | \\$$$  /  $$   ____|
   $$ |$$ |      $$ |$$ |  $$ |$$ | \\$$\\ \\$$$$$$$\\ $$ |$$\\   $$ |\\$$$$$$  |  \\$  /   \\$$$$$$$\\ 
   \\__|\\__|      \\__|\\__|  \\__|\\__|  \\__| \\_______|\\__|\\__|  \\__| \\______/    \\_/     \\_______|
================================================================================================
   
""", 'yellow'))
print(colored('Modele des données :', 'yellow'))
pprint(people[0])

# debut de l'exo
print(colored(''.join(['_' for _ in range(80)]), 'green', 'on_green'))

print(colored("Nombre d'hommes : ", 'yellow'))
# pour chaque personne du tableau, si son genre == 'Male' je le met dans le tableau hommes
hommes = [p for p in people if p['gender'] == 'Male']
# len() revoie la taille (nombre d'élément) d'un tableau
pprint(len(hommes))

################################################################################

# je peux aussi l'écrire avec une boucle classique
hommes2 = []                        # un tableau vide
for person in people:               # pour chaque persone du tableau
    if person["gender"] == "Male":  # si c'est un homme (2-266-02250-4)
        hommes2.append(person)      # je l'ajoute au tableau
print(len(hommes2))

################################################################################

# dans la même idée, plutot que de mettre tous les hommes dans un tableau
# puis afficher la longueur du tableau, je peux juste les compter dans une variable
nb_hommes = 0                       # je commence à 0
for person in people:               # pour chaque persone du tableau
    if person["gender"] == "Male":  # si c'est un homme
        nb_hommes = nb_hommes + 1   # j'ajoute 1 à mon compteur
print(nb_hommes)

################################################################################

print(colored("Nombre de femmes : ", 'yellow'))
# je peux compter les femmes ou calculer : nombre d'élement dans people - nombre d'homme
nb_femmes = 0
for person in people:
    if person["gender"] == "Female":
        nb_femmes = nb_femmes + 1
print(nb_femmes)

################################################################################

print(colored("Nombre de personnes qui cherchent un homme :", 'yellow'))
cherche_homme = 0
for person in people:
    if person ["looking_for"] == "M":
        cherche_homme = cherche_homme + 1
print(cherche_homme)

################################################################################

print(colored("Nombre de personnes qui cherchent une femme :", 'yellow'))

cherche_femme = 0
for person in people:
    if person ["looking_for"] == "F":
        cherche_femme = cherche_femme + 1
print(cherche_femme)

################################################################################

print(colored("Nombre de personnes qui gagnent plus de 2000$ :", 'yellow'))
cherche_p2000 = 0

for person in people: 
    income_str = person["income"]
    income_value = float(income_str.replace('$', '').replace(',', ''))

    if income_value > 2000:
        cherche_p2000 += 1

print(cherche_p2000)

################################################################################

print(colored("Nombre de personnes qui aiment les Drama :", 'yellow'))
# là il va falloir regarder si le chaine de charactères "Drama" se trouve dans "pref_movie"
cherche_drama = 0
for person in people:
    #check if the str "Drama" in "pref_movie"
    if "Drama" in person["pref_movie"]:
        cherche_drama += 1

print(cherche_drama)

################################################################################

print(colored("Nombre de femmes qui aiment la science-fiction :", 'yellow'))
# si j'ai déjà un tableau avec toutes les femmes, je peux chercher directement dedans ;)
women = []

#collect women in femmes_sf
for person in people:
    if person["gender"] == "Female":
        women.append(person)

#check if Sci-Fi
women_sf = 0
for person in women:
    if "Sci-Fi" in person["pref_movie"]:
        women_sf += 1

print(women_sf)

################################################################################

print(colored('LEVEL 2' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))

################################################################################

print(colored("Nombre de personnes qui aiment les documentaires et gagnent plus de 1482$", 'yellow'))

doc1482 = 0

for person in people:
    income_str = person["income"]
    income_value = float(income_str.replace('$', '').replace(',', ''))

    #check if the str "Documentary" in "pref_movie"
    if "Documentary" in person["pref_movie"] and income_value > 1482:
        doc1482 += 1

print(doc1482)

################################################################################

print(colored("Liste des noms, prénoms, id et revenus des personnes qui gagnent plus de 4000$", 'yellow'))

nb = 0
for person in people:

    income_str = person["income"]
    income_value = float(income_str.replace('$', '').replace(',', ''))

    if income_value > 4000:
        print(f"ID: {person['id']}, Nom: {person['last_name']}, Prénom: {person['first_name']}, Revenu: {person['income']}")
        nb += 1
        
print(nb)

################################################################################

print(colored("Homme le plus riche (nom et id) :", 'yellow'))
max_income = 0
richest_man = None #init empty var to store richest man

for person in people:
    income_str = person["income"]
    income_value = float(income_str.replace('$', '').replace(',', ''))
  
    if income_value > max_income and person["gender"] == "Male":
        max_income = income_value
        # richest_man = person #store person object

for person in people:
    income_str = person["income"]
    income_value = float(income_str.replace('$', '').replace(',', ''))
    if income_value == max_income: 
        print(f"ID: {person['id']}, Nom: {person['last_name']}")

# if richest_man:
#     print(f"ID: {person['id']}, Nom: {person['last_name']}")


################################################################################

print(colored("Salaire moyen :", 'yellow'))

total_income = 0
total_people = len(people)

for person in people:
    income_str = person["income"]
    income_value = float(income_str.replace('$', '').replace(',', ''))

    total_income += income_value #total_income = total_income + income_value

average = total_income / total_people

print(average)
print(f"${round(average, 2):,.2f}")

################################################################################

print(colored("Salaire médian :", 'yellow'))

incomes = []
for person in people:
    income_str = person["income"]
    income_value = float(income_str.replace('$', '').replace(',', ''))
    incomes.append(income_value)

#sort income
incomes.sort() 

#median is average of the 2 middle number ( n/2 )th and ((n/2 + 1))th values.

n = len(incomes)
median_income = (incomes[n // 2 -1] + incomes [n // 2]) / 2

print(median_income)

################################################################################

print(colored("Nombre de personnes qui habitent dans l'hémisphère nord :", 'yellow'))


p_north = 0

for person in people:
    if person["latitude"] > 0:
        p_north += 1

print(p_north)

################################################################################

print(colored("Salaire moyen des personnes qui habitent dans l'hémisphère sud :", 'yellow'))

income_south = 0
p_south = 0

for person in people:
    income_str = person["income"]
    income_value = float(income_str.replace('$', '').replace(',', ''))

    if person["latitude"] < 0:
        p_south += 1
        income_south += income_value #total_income = total_income + income_value

average_south = income_south / p_south

print(average_south)
print(f"${round(average_south, 2):,.2f}")

################################################################################

print(colored('LEVEL 3' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))

################################################################################

print(colored("Personne qui habite le plus près de Bérénice Cawt (nom et id) :", 'yellow'))

#distance is square root of coordinates sum DEFINE THE DISTANCE Fn
def distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

#find coordinates of Bérénice Cawt
lat2 = None #init vars
lon2 = None

for person in people:
    if person["first_name"] == "Bérénice" and person["last_name"] == "Cawt":
        lat2 = person["latitude"]       #store in a var
        lon2 = person["longitude"]
        break                           #exit loop once B C found

#init variables to store shortest distance and person detail
shortest_dist = float('inf')    #start with large number
closest_person = None

# parse the db and calculate distances by using the distance formula
for person in people:
    if person["first_name"] != "Bérénice" and person["last_name"] != "Cawt":  # Avoid comparing with Bérénice
            current_dist = distance(lat2, lon2, person["latitude"], person["longitude"])
            if current_dist < shortest_dist:
                shortest_dist = current_dist
                closest_person = person

if closest_person:
    print(f"ID: {closest_person['id']}, Nom: {closest_person['last_name']}, Prénom: {closest_person['first_name']}")

################################################################################

print(colored("Personne qui habite le plus près de Ruì Brach (nom et id) :", 'yellow'))

lat2 = None #init vars
lon2 = None

for person in people:
    if person["first_name"] == "Ruì" and person["last_name"] == "Brach":
        lat2 = person["latitude"]       #store in a var
        lon2 = person["longitude"]
        break                           #exit loop once found

#init variables to store shortest distance and person detail
shortest_dist = float('inf')    #start with large number
closest_person = None

# parse the db and calculate distances by using the distance formula
for person in people:
    if person["first_name"] != "Ruì" and person["last_name"] != "Brach":  # Avoid comparing with Bérénice
            current_dist = distance(lat2, lon2, person["latitude"], person["longitude"])
            if current_dist < shortest_dist:
                shortest_dist = current_dist
                closest_person = person

if closest_person:
    print(f"ID: {closest_person['id']}, Nom: {closest_person['last_name']}, Prénom: {closest_person['first_name']}")

################################################################################

print(colored("les 10 personnes qui habitent les plus près de Josée Boshard (nom et id) :", 'yellow'))


lat2 = None #init vars
lon2 = None

for person in people:
    if person["first_name"] == "Josée" and person["last_name"] == "Boshard":
        lat2 = person["latitude"]       #store in a var
        lon2 = person["longitude"]
        break                           #exit loop once found

shortest_dist = float('inf')  

list10 = []
for person in people:
    if person["first_name"] != "Josée" and person["last_name"] != "Boshard":  
            current_dist = distance(lat2, lon2, person["latitude"], person["longitude"])    
    list10.append((current_dist, person))
    list10.sort(key=lambda x: x[0]) #sort by distance
    if len(list10) > 10:
        list10.pop()

for current_dist, person in list10:
    print(f"ID: {person['id']}, Nom: {person['last_name']}, Prénom: {person['first_name']}")
################################################################################

print(colored("Les noms et ids des 23 personnes qui travaillent chez google :", 'yellow'))

for person in people:
    if "google" in person["email"]:
        print(f"ID: {person['id']}, Nom: {person['last_name']}, Prénom: {person['first_name']}")

################################################################################

print(colored("Personne la plus agée :", 'yellow'))

oldest = None

for person in people:
    if oldest is None or person["date_of_birth"] < oldest["date_of_birth"]:
        oldest = person                                    

################################################################################

print(colored("Personne la plus jeune :", 'yellow'))

youngest = None

for person in people:
    if youngest is

#############    
print(colored("Moyenne des différences d'age :", 'yellow'))



print(colored('HERE', 'yellow', 'on_red'))
################################################################################
print(colored('LEVEL 4' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))
################################################################################

print(colored("Genre de film le plus populaire :", 'yellow'))

#set up counter pour film 
#recupere les counters et les sort
#pop et garder le max
#print le nom du film

################################################################################

print(colored("Genres de film par ordre de popularité :", 'yellow'))

#use the previous counters and print 

################################################################################

print(colored("Liste des genres de film et nombre de personnes qui les préfèrent :", 'yellow'))

#print all counter titles and display counter

################################################################################

print(colored("Age moyen des hommes qui aiment les films noirs :", 'yellow'))

#list init
#if gender M calculate age 
#store in var and divide by value of counter

################################################################################

print(colored("Age moyen des femmes qui aiment les drames et habitent sur le fuseau horaire, de Paris : ", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("""Homme qui cherche un homme et habite le plus proche d'un homme qui a au moins une
préférence de film en commun (afficher les deux et la distance entre les deux):""", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Liste des couples femmes / hommes qui ont les même préférences de films :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored('MATCH' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))
"""
    On match les gens avec ce qu'ils cherchent (homme ou femme).
    On prend en priorité ceux qui ont le plus de gouts en commun.
    Puis ceux qui sont les plus proches.
    Les gens qui travaillent chez google ne peuvent qu'être en couple entre eux.
    Quelqu'un qui n'aime pas les Drama ne peux pas être en couple avec quelqu'un qui les aime.
    Quelqu'un qui aime les films d'aventure doit forcement être en couple avec quelqu'un qui aime aussi 
    les films d'aventure.
    La différences d'age dans un couple doit être inférieure à 25% (de l'age du plus agé des deux)
    ߷    ߷    ߷    Créer le plus de couples possibles.                  ߷    ߷    ߷    
    ߷    ߷    ߷    Mesurez le temps de calcul de votre fonction         ߷    ߷    ߷    
    ߷    ߷    ߷    Essayez de réduire le temps de calcul au maximum     ߷    ߷    ߷    

"""
print(colored("liste de couples à matcher (nom et id pour chaque membre du couple) :", 'yellow'))
print(colored('Exemple :', 'green'))
print(colored('1 Alice A.\t2 Bob B.'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))
```
