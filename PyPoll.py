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

# Prints to terminal - results per candidate- total votes, percentages
print('--------------------\nElection Results\n--------------------')
print(f'Total Votes: {votes_total}\n--------------------')
for candidate in election:
    print(f'{candidate}: {round(100*election[candidate]/votes_total,3)} % ({election[candidate]})')
print(f'--------------------\nWinner: {winning_candidate}\n--------------------')

# exports summary to a text file 
export = os.path.join("PyPoll","Analysis","Election_results.txt")
with open(export, 'w') as text:
    text.write('--------------------\nElection Results\n--------------------\n')
    text.write(f'Total Votes: {votes_total}\n--------------------\n')
    for candidate in election:
        text.write(f'{candidate}: {round(100*election[candidate]/votes_total,3)} % ({election[candidate]})\n')
    text.write(f'--------------------\nWinner: {winning_candidate}\n--------------------')