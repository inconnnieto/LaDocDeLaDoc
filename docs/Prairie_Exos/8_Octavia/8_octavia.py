import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

def asch(ref, A, B, C, rep): #verifie si la reponse est bonn
    if ref == A:
        if rep == 1:
            return True
        else:
            return False
    elif ref == B:
        if rep == 2:
            return True
        else:
            return False
    elif ref == C:
        if rep == 3:
            return True
        else:
            return False
    return False

# dataset   ref  A  B   C   rep
test_data_true = [10, 5, 10, 20, 2]
must_be_true = asch(*test_data_true) # same as content of []
print(must_be_true)

# dataset   ref  A  B   C   rep
test_data_false = [10, 5, 10, 20, 2]
must_be_false = asch(*test_data_false)
print(must_be_false)

#Le modèle du dataset d'entraînement

df = pd.read_csv("8_octavia_train_40.csv") #read dataset

import csv 
with open('8_octavia_train_40.csv') as csvfile:
    df = list(csv.reader(csvfile))
 
df = df[1:]
#doesnt change original table so need to make a temp table
df_temp = []

for l in df:
    l_temp = []
    for case in l:
        if case == "true":
            l_temp.append(1)
        else:
            l_temp.append(int(case))
    df_temp.append(l_temp)

df = df_temp

# print(df)

count = 1
for l in df:
    count += 1
    if asch(*l[:5]):
        pass
    else:
        print("problem!")
        print("line: ", count)
        print(l)

### ML if not imported yet import pandas, sklearn tree, sk learn decision tree, matplotlib
dataframe = pd.read_csv("8_octavia_train_35.csv")

features = ['ref','A','B','C','rep']

dataframe["valid"] = dataframe["valid"].map({True: 1, False: 0})

inputs = dataframe[features]
outputs = dataframe['valid']

dtree = DecisionTreeClassifier()

dtree = dtree.fit(inputs, outputs)

tree.plot_tree(dtree, feature_names=features)
plt.show()

print(dtree.predict([[10,10,3,9,1]]))