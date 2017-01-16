#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#count the poi's in the dataset
count = 0
for person_name in enron_data.keys():
    #print person_name
    if enron_data[person_name]["poi"] == 1:
	   count += 1
	   
	   
print "the no. of poi = ",count

#Data Query

#print enron_data['PRENTICE JAMES']['total_stock_value']
#print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
#print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

#find the person who got most of the money

#print max(enron_data['SKILLING JEFFREY K']['total_payments'], enron_data['LAY KENNETH L']['total_payments'],enron_data['FASTOW ANDREW S']['total_payments'])
temp = 0
for person in ['SKILLING JEFFREY K', 'LAY KENNETH L', 'FASTOW ANDREW S' ]:
  if enron_data[person]['total_payments'] > temp:
     temp = enron_data[person]['total_payments']
     accused = person
#print enron_data[accused]
print "The guy who got most of the money was ", accused, ". He got ", temp, " dollars"

#people with quantified salaries and no. with valid email adresses
email_count = 0; salaries_count = 0
for person in enron_data.keys():

    if enron_data[person]['email_address'] != 'NaN':
	   email_count += 1
	   
    if enron_data[person]['salary'] != 'NaN':
	   salaries_count += 1
	   

print "Number of persons with quantified Salaries is ", salaries_count
print "Number of persons with valid email address is ", email_count

