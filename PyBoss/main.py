#import csv

import os
import csv 

csvdata= os.path.join( "employee_data1.csv")



#abbreviation dictionary
stateabbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Lists
empid = []
firstname = []
lastname = []
birthday =[]
social = []
state = []

with open(csvdata, "r", newline= '') as csv_fileX:
    csvdata = csv.reader(csv_fileX, delimiter=',')
    next(csvdata, None)


    # loopi
    for row in csvdata:
        # appending employee ID
        empid.append(row[0])

        # split first namr from last and then append both
        name = row[1].split(" ") 
        firstname.append(name[0]) 
        lastname.append(name[1]) 

        # appending birthday
        birthday = row[2].split("-") 
        newbirthday =(row[2].split('-')[1] + '/' + row[2].split('-')[2] + '/' + row[2].split('-')[0])
        birthday.append(newbirthday)

         #appending social
        social = row[3].split("-") 
        new_ssn = ("***-**-" +social[2]) 
        social.append(new_ssn) 

        # loop dictionary to change to abbreviation
        state.append(stateabbrev[row[4]])

new_data = zip(empid, firstname, lastname, birthday, social, state)


#open and writes to csv
with open("PyBoss.csv", 'w') as csv_fileX:
    thisfile = csv.writer(csv_fileX, delimiter = ",")
    thisfile.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    thisfile.writerows(new_data)







