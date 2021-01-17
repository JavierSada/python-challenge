# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "PyBank","Resources", "budget_data.csv")

# Set variables
total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
month_change = 0
total_month_change = 0
average_month_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_increase_month = ""

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # count the total number of months
        total_months += 1
        
        # add up the total net profit/loss
        total_profit_loss += int(row[1])
        
        # calculate the change in profit/loss between months
        if total_months > 1:
            month_change = int(row[1]) - prev_profit_loss
            
        # add up the total monthly change, used later to calculate average
        total_month_change += month_change
        
        # set profit/loss value for previous month
        prev_profit_loss = int(row[1])
        
        # calculate greatest increase in profits
        if month_change > greatest_increase:
            greatest_increase = month_change
            greatest_increase_month = row[0]
        
        # calculate greatest decrease in losses
        if month_change < greatest_decrease:
            greatest_decrease = month_change
            greatest_decrease_month = row[0]

# calculate average change between months        
average_month_change = total_month_change / (total_months - 1)

# Print the analysis to terminal
print("Financial Analysis")
print("----------------------------")        
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit_loss))
print("Average Change: $" + str(format(average_month_change, '.2f')))
print("Greatest Increase in Profits: " + greatest_increase_month 
      + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_month 
      + " ($" + str(greatest_decrease) + ")")

# Write to text file
f = open("analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")        
f.write("Total Months: " + str(total_months) + "\n")
f.write("Total: $" + str(total_profit_loss) + "\n")
f.write("Average Change: $" + str(format(average_month_change, '.2f')) + "\n")
f.write("Greatest Increase in Profits: " + greatest_increase_month 
      + " ($" + str(greatest_increase) + ")\n")
f.write("Greatest Decrease in Profits: " + greatest_decrease_month 
      + " ($" + str(greatest_decrease) + ")\n")
f.close()