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
"""
{'salary': 'NaN',
'to_messages': 'NaN',
'deferral_payments': 564348,
'total_payments': 564348,
'exercised_stock_options':886231,
'bonus': 'NaN',
'restricted_stock': 208809,
'shared_receipt_with_poi': 'NaN',
'restricted_stock_deferred': 'NaN',
'total_stock_value': 1095040,
'expenses': 'NaN',
'loan_advances': 'NaN',
'from_messages': 'NaN',
'other': 'NaN',
'from_this_person_to_poi': 'NaN',
'poi': False,
'director_fees': 'NaN',
'deferred_income': 'NaN',
'long_term_incentive': 'NaN',
'email_address': 'james.prentice@enron.com',
'from_poi_to_this_person': 'NaN'}

"""
import pickle
from operator import itemgetter

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print 'Total no. of people in enron list: ',len(enron_data)
print 'Total no. of features for a person: ',len(enron_data.iteritems().next()[1])

count = 0
for key,value in enron_data.iteritems():
    if value['poi'] is True:
        count+=1
print 'No. of point of interest: ',count

# print 'Total value of the stock belonging to James Prentice:'
for key,value in enron_data.iteritems():
    if key.startswith('PRENTICE JAMES'):
        print 'Total value of the stock belonging to',key,' : ',value['total_stock_value']

for key,value in enron_data.iteritems():
    if key.startswith('COLWELL WESLEY'):
        print 'Total no. of the mails from',key,'to POI :',value['from_this_person_to_poi']

for key,value in enron_data.iteritems():
    if key.startswith('Skilling Jeffrey K'.upper()):
        print 'Value of stock options exercised by',key,':',value['exercised_stock_options']

payments = []
for key,value in enron_data.iteritems():
    if value['total_payments'] != "NaN":
        payments.append({'name':key,'payment':value['total_payments']})
newlist = sorted(payments, key=lambda k: k['payment'])
print "Guy who came away with most of the money :",newlist[len(newlist)-2]

