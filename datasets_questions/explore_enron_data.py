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


print 'Total no. of people in enron list: ',len(enron_data)
print 'Total no. of features for a person: ',len(enron_data.iteritems().next()[1])

count = 0
for key,value in enron_data.iteritems():
	if value['poi'] is True:
		count+=1
print 'No. of point of interest: ',count

