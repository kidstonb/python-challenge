# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:
import os 
import csv

# variable initialization 
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

# Print of results per candidate- total votes, percentages
print('--------------------\nElection Results\n--------------------')
print(f'Total Votes: {votes_total}\n--------------------')
for candidate in election:
    print(f'{candidate}: {round(100*election[candidate]/votes_total,3)} % ({election[candidate]})')

# * The winner of the election based on popular vote.
winner = 0
for candidate in election:
    if 
print('--------------------\nWinner: {}\n--------------------')

# Your analysis should look similar to the following:


#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 369711
#   -------------------------
#   Charles Casper Stockham: 23.049% (85213)
#   Diana DeGette: 73.812% (272892)
#   Raymon Anthony Doane: 3.139% (11606)
#   -------------------------
#   Winner: Diana DeGette
#   -------------------------
#   ```

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.