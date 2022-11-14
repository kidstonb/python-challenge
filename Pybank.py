import csv
import os 

# variables initialization
greatest_profit = 0 
lowest_profit = 0 
profit_list = []
change_list = []

csv_path = os.path.join("PyBank","Resources","budget_data.csv")

with open(csv_path,'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    for row in csv_reader:
        
        # Collect all the profit data into a list 
        profit_list.append(int(row[1]))

        # * The greatest increase and decrease in profits (date and amount) over the entire period
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

# prints summary to terminal
print('----------------------------\nFinancial Analysis\n----------------------------')
print(f'Total Months: {len(profit_list)}')      
print(f'Total: ${sum(profit_list)}')                    
print(f'Average Change: ${round(average_change,2)}')
print(f'Greatest Increase in Profits: {greatest_date} (${greatest_profit})')
print(f'Greatest Decrease in Profits: {lowest_date} (${lowest_profit})')
print('----------------------------')

# exports to a text file
export = os.path.join("PyBank","Analysis","Financial_Analysis.txt")
with open(export, 'w') as text:
    text.write('----------------------------\nFinancial Analysis\n----------------------------\n')
    text.write(f'Total Months: {len(profit_list)}\n')      
    text.write(f'Total: ${sum(profit_list)}\n')                   
    text.write(f'Average Change: ${round(average_change,2)}\n')
    text.write(f'Greatest Increase in Profits: {greatest_date} (${greatest_profit})\n')
    text.write(f'Greatest Decrease in Profits: {lowest_date} (${lowest_profit})\n')
    text.write('----------------------------')
