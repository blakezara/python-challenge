

import os
import csv 

csvdata= os.path.join("election_data_1.csv")


# Variables
total_votes = 0
winner = 0



#Lists
candidates =[]
votes =[]

# dictionary in order to find percent (list indices unordered)
vote_percent ={}


# Dictionary for Keys and Values row2 is key row1 as total count/value?
the_poll = {}

#open files 

with open(csvdata, "r", newline= '') as csv_fileX:
    csvdata = csv.reader(csv_fileX, delimiter=',')
    next(csvdata, None)
    
#Loop to count candidates
    for row in csvdata:
        total_votes += 1
        if row[2] in the_poll.keys():
            the_poll[row[2]] = the_poll[row[2]] + 1
        else:
            the_poll[row[2]]= 1 


# append the keys (candidates) and values (votes)
    for key, value in the_poll.items():
        candidates.append(key)
        votes.append(value)
        
        

#find vote percent of votes with the dictionary
    for key, value in the_poll.items():
        vote_percent[key] = round((value)/(total_votes)*100, 2)
        
        

#create new list with appended lists using zip
the_poll_final = zip(candidates, votes, vote_percent)


#find winner
for total_votes in the_poll_final:
    winner = max(vote_percent)


with open("PyPoll.csv", 'w') as csv_fileX:
    thisfile = csv.writer(csv_fileX, delimiter = ",")
    thisfile.writerow(['Candidates', 'Votes', 'Percent of Votes'])
    thisfile.writerows(the_poll_final)







