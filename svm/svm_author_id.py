#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
from sklearn import svm
from sklearn.metrics import accuracy_score

clf = svm.SVC(C = 10000,kernel = 'rbf')

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()- t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "Prediction time:", round(time()- t1, 3), "s"

accuracy = accuracy_score(labels_test, pred)
print "accuracy = ", accuracy*100, "%"

#check prediction labels
print "prediction for 10th element = ", pred[10]
print "prediction for 26th element = ", pred[26]
print "prediction for 50th element = ", pred[50]

#no. of chris's emails
count = 0
for x in pred:
  if x == 1:
    count += 1
print "No. of chris's emails = ", count


#########################################################


