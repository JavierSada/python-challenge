import os 
import csv
#path to the csvfile
csvpath = os.path.join('election_data.csv')

#initializing the variables 
poll_data={}
total_votes = 0
with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)

    for row in csvread:
        total_votes += 1
        if row[2] in poll_data.keys():
            poll_data[row[2]] = poll_data[row[2]] + 1
        else:
            poll_data[row[2]] = 1 
    

candidates = []  
tot_num_votes = []
# Total Number of votes
for key, value in poll_data.items():
    candidates.append(key)
    tot_num_votes.append(value)
  
# Percentage of votes
percentage_votes =[]
for n in tot_num_votes:
    percentage_votes.append(round(n/total_votes * 100, 1))
 
# Finding the winner
clean_data = list(zip(candidates, tot_num_votes, percentage_votes))

winner_list = []
for name in clean_data:
    if max(tot_num_votes) == name[1]:
        winner_list.append(name[0])
winner = winner_list[0]

# Print all data
print ("Election results :")
print(total_votes) 
print(candidates)  
print(percentage_votes)
print(tot_num_votes)  
print(winner)

# Writng output files
PyPoll = open("output.txt","w+")
PyPoll.write("Election Results")  
PyPoll.write('\n' + "Total_votes" + str(total_votes)) 
PyPoll.write('\n' + str(candidates))
PyPoll.write('\n' + str(percentage_votes))
PyPoll.write('\n' + str(tot_num_votes)) 
PyPoll.write('\n' + "Winner:" + winner) 