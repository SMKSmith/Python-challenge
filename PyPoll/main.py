#Import modules
import os, csv

#Specify file path to read
csv_path = os.path.join(".", "Resources", "election_data.csv")

#Set dictionary for canidates
canidates = {}

#Open file in reader status
with open(csv_path) as csv_file:
    
    #Read csv file and set delimiter value to ","
    csv_reader = csv.reader(csv_file, delimiter= ",")

    #Read the row with header first
    csv_header = next(csv_reader)

    #Set initial value for total votes to zero
    vote_total = 0

    #Iterate through data
    for row in csv_reader:
        
        #Count all votes
        vote_total += 1
        
        #Set start location for canidate_name is column 3
        canidate_name= row[2]

        #Set conditions to initiate loop
        if canidate_name in canidates:
            
            #Increase by one to move to next row of data 
            canidates[canidate_name] += 1
        
        #Set condition to stop iteration
        else:
            canidates[canidate_name] = 1

#Calculate percentage of votes per canidate based on keys for canidates dictionary
canidates["stockham"] = round((canidates["Charles Casper Stockham"]/vote_total) * 100, 3)
canidates["deGette"] = round((canidates["Diana DeGette"]/vote_total) * 100, 3)
canidates["raymon"] = round((canidates["Raymon Anthony Doane"]/vote_total) * 100, 3)

#Set variable and value for election winner
election_winner = max(canidates, key=canidates.get)

#Create varable for header line output
header_line = ("-------------------------")

#Print to add space to previous text
print(" ")

#Output header
print("Election Results")

#Output header line
print(header_line)

#Output total votes amount
print("Total Votes: " + str(vote_total))

#Output header line
print(header_line)

#Output election results
print("Charles Casper Stockham: " + str(canidates["stockham"]) + "% " + "(" + str(canidates["Charles Casper Stockham"]) + ")" )
print("Diana DeGette: " + str(canidates["deGette"]) + "% " + "(" + str(canidates["Diana DeGette"]) + ")")
print("Raymon Anthony Doane: " + str(canidates["raymon"]) + "% " + "(" + str(canidates["Raymon Anthony Doane"]) + ")" )

#Output header line
print(header_line)

#Output election winner
print("Winner: " + str(election_winner))

#Output header line
print(header_line)

#Set variable for file pathway
results = os.path.join(".", "analysis" , "election_results.txt")

#Oppen file to write to file
with open(results, "w") as py_file:

    #Write statesment to election_results.txt file 
    py_file.write("Election Results" + "\n")
    py_file.write(str(header_line) + "\n")
    py_file.write("Total Votes: " + str(vote_total) + "\n")
    py_file.write(str(header_line) + "\n")
    py_file.write("Charles Casper Stockham: " + str(canidates["stockham"]) + "% " + "(" + str(canidates["Charles Casper Stockham"]) + ")" + "\n")
    py_file.write("Diana DeGette: " + str(canidates["deGette"]) + "% " + "(" + str(canidates["Diana DeGette"]) + ")" + "\n")
    py_file.write("Raymon Anthony Doane: " + str(canidates["raymon"]) + "% " + "(" + str(canidates["Raymon Anthony Doane"]) + ")" + "\n")
    py_file.write(str(header_line) + "\n")
    py_file.write("Winner: " + str(election_winner)+ "\n")
    py_file.write(str(header_line) + "\n")
    py_file.close() 







