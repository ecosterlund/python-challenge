#Import Functions
import os
import csv

#telling Python where to access the csv data base to read it
py_bank_csv = os.path.join("PyBank", "resources", "budget_data.csv")

#lists to store months and profit/losses values
months_list = []
profit_losses =[]
avg_rev_change=[]
max_rev_change=[]
min_rev_change =[]
rev_change =[]
date = []
#READ INPUT FILE: budget_data.csv
#open the file as a csv file to read
with open(py_bank_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    #skip header
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")
    for line in csv_reader:
        #Calculates total months values
        months_list.append(f"{line[0]}")
        profit_losses.append(f"{line[1]}")
        date.append(f"{line[0]}")
    #Calculates Changes in Revenue
    for i in range(1,len(profit_losses)):
        #Starts comparison of profits/losses from previous row
        profit_losses = [ int(i) for i in profit_losses]
        rev_change.append(profit_losses[i] - profit_losses[i-1])
        #Calculates Average Revenue change
        avg_rev_change = round((sum(rev_change)/len(rev_change)), 2)
        #Calculates Greatest increase in profits
        max_rev_change = max(rev_change)
        #Calculates Greatest Decrease in profits
        min_rev_change = min(rev_change)
        #Stores Date values for output (List index out of range error)
        avg_rev_change_date = str(date[rev_change.index(max(rev_change))+1])
        max_rev_change_date = str(date[rev_change.index(max(rev_change))+1])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))+1])

    #BEGINNING OF TERMINAL OUTPUT
    #Prints "Financial Analysis"
    print("Financial Analysis")
    #Prints ------ to seperate title
    print("----------------------------")
    #Prints total number of months 
    print('Total Months: '+ str(len(months_list)))
    #Prints Total profit/losses summed up together
    profit_losses =[ int(x) for x in profit_losses]
    print("Total: $", sum(profit_losses))
    #Prints Rev Changes 
    print("Average Change: " + avg_rev_change_date, avg_rev_change)
    print("Greatest Increase in Profits: " + max_rev_change_date, max_rev_change)
    print("Greastest Decrease in Profits: " + min_rev_change_date, min_rev_change)

#OUTPUT ANALYSIS TO TXT FILE IN "ANALYSIS" FOLDER
#Define Output File Path
pybank_output_path = os.path.join("PyBank", "analysis", "pyBank_analysis.txt")
outputfile = open(pybank_output_path, "x")
outputfile.write("Financial Analysis\n")
outputfile.write("----------------------------\n")
outputfile.write("Total Months: ")
outputfile.write(str(len(months_list)))
outputfile.write("\n")
outputfile.write("Total: $")
outputfile.write(str(sum(profit_losses)))
outputfile.write("\n")
outputfile.write("Average Change: $")
outputfile.write(str(avg_rev_change))
outputfile.write("\n")
outputfile.write("Greatest Increase in Profits: ")
outputfile.write(str(max_rev_change_date))
outputfile.write("  $")
outputfile.write(str(max_rev_change))
outputfile.write("\n")
outputfile.write("Greatest Decrease in Profits: ")
outputfile.write(str(min_rev_change_date))
outputfile.write("  $")
outputfile.write(str(min_rev_change))
outputfile.write("\n")
