# 7_Septima 
## Python algo trinker - matchmaking algorithm

#### task:
implement serveral function to process and analyse a dataset for a dating app

#### goal:
implement code that provides answers to each of the questions, using data from `people.json` file

If you want to run the Python script, check the repo [here]()

## my attempt

#### importing in python

```python
import json
from pprint import pprint
from termcolor import colored
import math
```
#### loading .json file
As the data in the .json contained special characters that did not display well, it was necessary to specify here the `encoding='utf-8'` to be able to call data later

```python 
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
```

### Sorting and filtering through data
ways to do it

```python
hommes = [p for p in people if p['gender'] == 'Male']
pprint(len(hommes))
```
using a loop

```python
hommes2 = []                        # init empty list
for person in people:               
    if person["gender"] == "Male":  
        hommes2.append(person)      
print(len(hommes2))
```

using a counter
```python
nb_hommes = 0                       # init counter to 0
for person in people:               
    if person["gender"] == "Male":  
        nb_hommes = nb_hommes + 1   
print(nb_hommes)
```
same can be done for women
```python
nb_femmes = 0
for person in people:
    if person["gender"] == "Female":
        nb_femmes = nb_femmes + 1
print(nb_femmes)
```
### Criteria filtering
if looking for a man
```python
cherche_homme = 0
for person in people:
    if person ["looking_for"] == "M":
        cherche_homme = cherche_homme + 1
print(cherche_homme)
```

### Movie preferences
using Python's `in` operator to check if prefered genre was present in `pref_movie` list for each person

number of people who like Drama
```python
cherche_drama = 0
for person in people:
    #check if the str "Drama" in "pref_movie"
    if "Drama" in person["pref_movie"]:
        cherche_drama += 1
print(cherche_drama)
```
women who like sci-fi
```python
print(colored("Nombre de femmes qui aiment la science-fiction :", 'yellow'))

women = []
for person in people:
    if person["gender"] == "Female":
        women.append(person)

#check if Sci-Fi
women_sf = 0
for person in women:
    if "Sci-Fi" in person["pref_movie"]:
        women_sf += 1
print(women_sf)
```
### salary
Convert income string to float, removing the $ currency sign. 
Then compare it against thresholds.
Number of people who earn more than $2000
```python
cherche_p2000 = 0
for person in people: 
    income_str = person["income"]
    income_value = float(income_str.replace('$', '').replace(',', ''))

    if income_value > 2000:
        cherche_p2000 += 1

print(cherche_p2000)
```

## LEVEL 2 algo
### combined conditions
who like documentaries and earn more than $1482

```python
doc1482 = 0

for person in people:
    income_str = person["income"]
    income_value = float(income_str.replace('$', '').replace(',', ''))

    #check if the str "Documentary" in "pref_movie"
    if "Documentary" in person["pref_movie"] and income_value > 1482:
        doc1482 += 1
print(doc1482)
```
### Income Analysis
Convert income string to float, removing the $ currency sign.

Then compare it against thresholds.
List of name, first name, id income of people who earn more than $4000

```python
nb = 0
for person in people:
    income_str = person["income"]
    income_value = float(income_str.replace('$', '').replace(',', ''))

    if income_value > 4000:
        print(f"ID: {person['id']}, Nom: {person['last_name']}, Prénom: {person['first_name']}, Revenu: {person['income']}")
        nb += 1
        
print(nb)
```
### Richest man
```python
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
```
### Average salary
```python
total_income = 0
total_people = len(people)

for person in people:
    income_str = person["income"]
    income_value = float(income_str.replace('$', '').replace(',', ''))

    total_income += income_value #total_income = total_income + income_value

average = total_income / total_people

print(average)
print(f"${round(average, 2):,.2f}")
```
### Median salary
```python
incomes = []
for person in people:
    income_str = person["income"]
    income_value = float(income_str.replace('$', '').replace(',', ''))
    incomes.append(income_value)

incomes.sort()      #sort income

#median is average of the 2 middle number ( n/2 )th and ((n/2 + 1))th values.

n = len(incomes)
median_income = (incomes[n // 2 -1] + incomes [n // 2]) / 2

print(median_income)
```
### Geographical data
check if latitude attribute above or below 0.
Number of people living in the Northen hemisphere:
```python
p_north = 0
for person in people:
    if person["latitude"] > 0:
        p_north += 1
print(p_north)
```
### combined
average salary of people living in the southern hemisphere
```python
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
```
rounding off to 2 decimal places
```python
print(f"${round(average_south, 2):,.2f}")
```

## LEVEL 3

### Finding nearest people
implementation of distance function using Pythagoras' Theorem based on latitude and logitude. then compated distances to all people, making sure not to compare to the user mentioned itself, iteration to find the smallest distance

person living closest to Bérénice Cawt (name, id)
```python

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
```
10 people living closest to Josée Boshard
```python
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
```
Name and id of 23 people working at Google
```python
for person in people:
    if "google" in person["email"]:
        print(f"ID: {person['id']}, Nom: {person['last_name']}, Prénom: {person['first_name']}")
```
