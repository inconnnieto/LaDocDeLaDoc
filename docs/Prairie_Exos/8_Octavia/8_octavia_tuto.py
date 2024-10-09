import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv") #read dataset #in csv everything is a str

#make the dataset numerical
d = {'UK': 0, 'USA':1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

#separate feature(preditc from) from target column(values will try to predict)
#x is feature and y target
features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features] #features is column. X is input
y = df['Go'] # output

#create and display decision tree import modules sklearn

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y) #fit is training

tree.plot_tree(dtree, feature_names=features)

plt.show()