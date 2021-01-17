#Import Functions
import os
import csv

#telling Python where to access the csv data base to read it
py_poll_csv = os.path.join('PyPoll/resources/election_data.csv')

#Lists/Variables to store calculations
voter_id = []
county = []
candidate = []
total_votes = []
candidate_who_got_votes = []
percent_votes_won = []
total_votes_per_candidate = []
winner = []
#Defining function to calculate and print precentage of vote won for each candidate and store them in a dictionary?-------NECESSARY?
#def print_percentages(election_data):
    #Find total number of votes per candidate
    #Find percentage of votes received/total

#READ INPUT FILE: budget_data.csv
#open the file as a csv file to read
with open(py_poll_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    #skip header
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")
    for line in csv_reader:
        voter_id.append(f"{line[0]}")
        county.append(f"{line[1]}")
        candidate.append(f"{line[2]}")
    
    for i in range(1,len(voter_id)):
        #Complete list of candidates who received votes (conditional to weed out those who didn't get any?)
        
        #Calculates Percentage of votes each candidate won
        percent_votes_won = (total_votes_per_candidate/len(voter_id)) * 100))
        #Calculates total number of votes each candidate won (Use if statement like if name == candidate's name, calculate and store into variable for that candidate)

        #Winner of election (conditional for finding who has the most votes)

    #PRINT OUTPUT TO TERMINAL HERE
    #Print "Election Results"
    print("Election Results")
    #Print ----- to seperate title
    print("-------------------------")
    #Print Total Votes
    total_votes = len(voter_id)
    print("Total Votes: " + str(total_votes))
    #Print ----- to seperate votes from rest of data
    print("-------------------------")
    #Print list of each candidate, vote percentage, and total votes per candidate

    #Print ---- to seperate winner
    print("-------------------------")
    #Print Winner's Name

    #Print ---- to end terminal output
    print("-------------------------")

#OUTPUT FILE (File IO Error, used to work before updating reader code)
#Specify Output File Path
#pypoll_output = os.path.join('PyPoll/analysis/pypoll_analysis.csv')
#Open the output file using "write" mode.
#with open (pypoll_output, "w", newline='') as pypoll_analysis:
    #Initialize csv.writer
    #csv_writer = csv.writer(pypoll_analysis)

    #write in what the output should look like here
    #Print "Election Results"

    #Print Dashes to separate title

    #Print Total Votes:

    #Print Dashes to separate title

    #Print List of candidates with Name, percent of vote, and total votes they had
    #--------MAYBE USE DICTIONARY??-----

    #Print Dashes to separate analysis from the winner

    #Print the winner of the election

    #Print Dashes to end the analysis



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