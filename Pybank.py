# Your task is to create a Python script that analyzes the records to calculate each of the following:
import csv
import os 

# intialize values 
total_months = 0 
P_L = 0 
Increase = 0 
Decrease = 0 

filepath = os.path.join("PyBank","Resources","budget_data.csv")

with open(filepath,'r') as csvfile
    csvreader = csv.reader(csvfile,delimiter=',')
    #header = next(csvreader)


# * The total number of months included in the dataset

# * The net total amount of "Profit/Losses" over the entire period

# * The changes in "Profit/Losses" over the entire period, and then the average of those changes

# * The greatest increase in profits (date and amount) over the entire period

# * The greatest decrease in profits (date and amount) over the entire period

# Your analysis should look similar to the following:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $22564198
#   Average Change: $-8311.11
#   Greatest Increase in Profits: Aug-16 ($1862002)
#   Greatest Decrease in Profits: Feb-14 ($-1825558)
#   ```

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.