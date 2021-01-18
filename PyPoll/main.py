#Import Functions
import os
import csv

#telling Python where to access the csv data base to read it
py_poll_csv = os.path.join("PyPoll", "resources", "election_data.csv")

#Lists/Variables to store calculations
total_votes = []
winner = []
khan_votes = []
otooley_votes=[]
correy_votes=[]
li_votes = []

#READ INPUT FILE: budget_data.csv
#open the file as a csv file to read
with open(py_poll_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    #skip header
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")
    #Define content from csv to count for each candidate
    content = csv_file.read()
    #Counts the amount of times "Khan" appears in the list
    khan_votes = content.count("Khan")
    #Counts the amount of times "O'Tooley" appears in the list
    otooley_votes = content.count("O'Tooley")
    #Counts the amount of times "Li" appears in the list
    li_votes = content.count("Li")
    #Counts the amount of times "Correy" appears in the list
    correy_votes = content.count("Correy")
    #Calculates total votes
    total_votes = khan_votes + li_votes + correy_votes + otooley_votes
    #Prints individual vote numbers
    #print(khan_votes)
    #print(otooley_votes)
    #print(li_votes)
    #print(correy_votes)
    #Calculates Khan Vote Percentage
    khan_vote_percent = round(((khan_votes / total_votes) * 100), 2)
    #Calculates Correy Vote Percentage
    correy_vote_percent = round(((correy_votes / total_votes) * 100), 2)
    #Calculates Li Vote Percentage
    li_vote_percent = round(((li_votes / total_votes) * 100), 2)
    #Calculates O'Tooley Vote Percentage
    otooley_vote_percent = round(((otooley_votes / total_votes) * 100), 2)
    #print(khan_vote_percent)

    #PRINT OUTPUT TO TERMINAL HERE
    #Print "Election Results"
    print("Election Results")
    #Print ----- to seperate title
    print("-------------------------")
    #total_votes = len(list(csv_reader))----------Gives 0 value for all other individual votes
    #Print Total Votes
    print("Total Votes: " + str(total_votes))
    #Print ----- to seperate votes from rest of data
    print("-------------------------")
    #Print Khan results to terminal
    print("Khan: " + str(khan_vote_percent) + "%" " (" + str(khan_votes) + ")")
    #Print Correy results to terminal
    print("Correy: " + str(correy_vote_percent) + "%" " (" + str(correy_votes) + ")")
    #Print Li results to terminal
    print("Li: " + str(li_vote_percent) + "%" " (" + str(li_votes) + ")")
    #Print O'Tooley results to terminal
    print("O'Tooley: " + str(otooley_vote_percent) + "%" " (" + str(otooley_votes) + ")")
    
#OUTPUT TO TERMINAL AND CSV FILE SHOULD LOOK LIKE THIS
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#----------------------