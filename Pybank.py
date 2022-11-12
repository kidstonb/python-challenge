# Your task is to create a Python script that analyzes the records to calculate each of the following:
# import pandas - try not to use for this assignment
import csv 
import os 

# variables initialization
# total_months = 0 
# P_L = 0 
greatest_profit = 0 
lowest_profit = 0 
profit_list = []
change_list = []

csv_path = os.path.join("PyBank","Resources","budget_data.csv")

#with open(csv_pathpath,'r') as csvfile
with open(csv_path,'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)
    # print(f"CSV Header: {csv_header}")

    for row in csv_reader:
        # * The total number of months included in the dataset
        total_months += 1
        #print(type(int(row[1])))

        # * The net total amount of "Profit/Losses" over the entire period
    # Try to check if any inconsistencies in the dates?
        P_L += int(row[1])
        # Here I collect 
        profit_list.append(int(row[1]))

        # * The greatest increase in profits (date and amount) over the entire period
        # * The greatest decrease in profits (date and amount) over the entire period
        if int(row[1]) > greatest_profit:
            greatest_profit = int(row[1])
            greatest_date = row[0]
        if int(row[1]) < lowest_profit:
            lowest_profit = int(row[1])
            lowest_date = row[0]

# * The changes in "Profit/Losses" over the entire period, and then the average of those changes
for i in range(len(profit_list)-1):
    change_list.append(profit_list[i+1] - profit_list[i])

average_change = sum(change_list) / len(change_list)

print('----------------------------\nFinancial Analysis\n----------------------------')
print(f'Total Months: {len(profit_list)}')      # or just len(profit_list) or total_months
print(f'Total: ${sum(profit_list)}')                     # or sum(profit_list) or P_L
print(f'Average Change: ${round(average_change,2)}')
print(f'Greatest Increase in Profits: {greatest_date} (${greatest_profit})')
print(f'Greatest Decrease in Profits: {lowest_date} (${lowest_profit})')
print('----------------------------')

# output_path = os.path.join("output", "Financial_Analysis.txt")
# with open(output_path, 'w') as csvfile:


# * The changes in "Profit/Losses" over the entire period, and then the average of those changes

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.



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

