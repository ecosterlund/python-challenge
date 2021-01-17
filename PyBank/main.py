#Import Functions
import os
import csv

#telling Python where to access the csv data base to read it
py_bank_csv = os.path.join('PyBank/resources/budget_data.csv')

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
        #Calculates total months values (trying to count how many rows are in the list)
        months_list.append(f"{line[0]}")
        profit_losses.append(f"{line[1]}")
        date.append(f"{line[0]}")
    #Calculates Changes in Revenue
    for i in range(1,len(profit_losses)):
        profit_losses = [ int(i) for i in profit_losses]
        rev_change.append(profit_losses[i] - profit_losses[i-1])
        #Calculates Average Revenue change
        avg_rev_change = sum(rev_change)/len(rev_change)
        #Calculates Greatest increase in profits
        max_rev_change = max(rev_change)
        #Calculates Greatest Decrease in profits
        min_rev_change = min(rev_change)
        #Stores Date values for output (List index out of range error)
        avg_rev_change_date = str(date[rev_change.index(max(rev_change))+1])
        max_rev_change_date = str(date[rev_change.index(max(rev_change))+1])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))+1])
    #change_index = 
    print(rev_change.index(max(rev_change)))
    print(date[24])

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
    #Prints Rev Changes --------------------------------------------------------------MONTHS ARE OFF
    print("Average Change: " + avg_rev_change_date, avg_rev_change)
    print("Greatest Increase in Profits: " + max_rev_change_date, max_rev_change)
    print("Greastest Decrease in Profits: " + min_rev_change_date, min_rev_change)

#print(len(date))
#print(len(rev_change))
#for i in zip(date, rev_change):
    #print(i)


#OUTPUT FILE (File IO Error, used to work before updating reader code)--------------------------ASK
#Specify Output File Path
pybank_output = os.path.join("PyBank", "analysis", "PyBank_analysis.csv" )
#Open the output file using "write" mode.
with open (pybank_output, "w", newline='') as pybank_analysis:
    #Initialize csv.writer
    csv_writer = csv.writer(pybank_analysis, delimiter = ',')

    #write in what the output should look like here
    #"Financial Analysis"
    csv_writer.writerow(months_list)
    #Dashes to separate the title
    csv_writer.writerow('----------------------------')
    #Print "Total Months: "

    #Print Total:

    #Print Average Change:

    #Print Greatest Increase in Profits:

    #Prints Greatest Decrease in Profits

#WHAT THE OUTPUT SHOULD LOOK LIKE IN THE CSV FILE AND TERMINAL
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
