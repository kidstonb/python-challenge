# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

import os 
import csv

# dictionary initialization 
election = {}

csv_path = os.path.join("PyPoll","Resources","election_data.csv")

with open(csv_path,'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    # Adds candidate to dictionary if not present, otherwise increments the vote for that candidate
    for row in csv_reader:
        if row[2] not in election:
            election[row[2]] = 1
        else:
            election[row[2]] += 1
    
# Totals the votes from the dictionary
votes_total = sum(election.values())

# * The winner of the election based on popular vote.
max_vote = 0 
for candidate in election:
    if election[candidate] > max_vote:
        winning_candidate = candidate
        max_vote = election[candidate]

# Print of results per candidate- total votes, percentages
print('--------------------\nElection Results\n--------------------')
print(f'Total Votes: {votes_total}\n--------------------')
for candidate in election:
    print(f'{candidate}: {round(100*election[candidate]/votes_total,3)} % ({election[candidate]})')
print(f'--------------------\nWinner: {winning_candidate}\n--------------------')

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.