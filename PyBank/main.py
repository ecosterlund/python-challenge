#Import Functions
import os
import csv

#telling Python where to access the csv data base to read it
py_bank_csv = os.path.join('PyBank/resources/budget_data.csv')


#READ INPUT FILE: budget_data.csv
#open the file as a csv file to read
with open(py_bank_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    #skip header
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")
    for row in csv_reader:
        #lists to store months and profit/losses values
        months_list = row[0]
        profit = [1]
        profit_losses =[]
        greatest_profit_increase = []
        total_monthly_change = []
        #Calculates total months values (trying to count how many rows are in the list)
        print('Total Months: '+ str(len(months_list)))
        #Calculates the Total profit/losses added up from each row

        #Calculates Average Change

        #Calculates Greatest increase in profits

        #Calculates Greatest Decrease in profits

#OUTPUT FILE (File IO Error, used to work before updating reader code)
#Specify Output File Path
#pybank_output = os.path.join('PyBank/analysis/pybank_analysis.csv')
#Open the output file using "write" mode.
#with open (pybank_output, "w", newline='') as pybank_analysis:
    #Initialize csv.writer
    #csv_writer = csv.writer(pybank_analysis)

    #write in what the output should look like here
    #"Financial Analysis"
    #csv_writer.writerow('Financial Analysis')
    #Dashes to separate the title
    #csv_writer.writerow('----------------------------')
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
