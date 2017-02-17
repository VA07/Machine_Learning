#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]


data = featureFormat(data_dict, features_list)

labels, features = targetFeatureSplit(data)

#print labels

### your code goes here 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size = 0.3, random_state = 42)

#biased prediction , predict non-poi for all
p = [0 for i in enumerate(x_test)]

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

#number of POI's
print(len([label for label in y_test if label == 1.0 ]))

#no. of people in test set
print (len(y_test))
	
#accuracy  
accuracy = accuracy_score(y_test, y_pred)
print "accuracy = ", accuracy*100, "%"

#precision and recall
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
print ("Precision = "), (precision_score(y_test, y_pred, average='micro'))
print ("Recall = "), (recall_score(y_test, y_pred, average=None))


