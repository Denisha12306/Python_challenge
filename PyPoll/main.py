import os 
import csv

#Input data file path
election_csv = os.path.join("..","Resources","Election_data.csv")


#Total Vote Counter
total_votes=0

#Candidate options list
candidate_options=[]

#Vote counter dictionary
candidate_votes={}

#Set variables to track Winning Candidate and Winning Count
winning_candidtae=""
winning_count=0

#Open and read the csv and convert it into list of dictionaries

with open(election_csv) as election_data:
    reader=csv.DictReader(election_data)

    #Loop through for each row
    
    for row in reader:

        #Add to the total vote count
        total_votes=total_votes+1

        #Extract the candidate name from each row
        candidate_name=row["Candidate"]

        #If the candidate name does not match any excisting candidate
        if candidate_name not in candidate_options:

            #Add it to the list of candidtes in the running
            candidate_options.append(candidate_name)

            #Then start to track that candidate's voter count
            candidate_votes[candidate_name]=0

        #Then add a vote to that candidate's voter count
        candidate_votes[candidate_name]=candidate_votes[candidate_name]+1


                                  
    
    #Print the final vote count
    election_results= (
        f"\n\nElection Results\n"
        f".....................\n"
        f"Total Votes:{total_votes}\n"
        f"..........................\n"
    )
    
    
    print(election_results)

   
     #Path to save election results file to analysis folder in Pypoll

    election_results=os.path.join("..","Analysis","election_results.txt")
                                  
    #Save the final vote count to the output file
    with open("election_results.txt","a")as f:
        f.write(election_results)


    #Ditermine the wiinner by looping through the counts
    for candidate in candidate_votes:

        #Retrieve the vote count and percentage

        votes=candidate_votes.get(candidate)
        votes_percentage=float(votes)/float(total_votes)*100

        #Determine winning vote count and candidtae
        if(votes>winning_count):
            winning_count=votes
            winning_candidate=candidate

         #Print each candidate's voter count and percentage
        voter_output=f"{candidate}:{votes_percentage:.3f}%({votes})\n"
        print(voter_output)

        #Save each candidate's voter count and percentage to text file
        with open("election_results.txt","a")as f:
            f.write(voter_output)
            

        
    
    #Print the winning candidate

    winning_candidate_summary= (
         f"......................\n"
         f"Winner:{winning_candidate}\n"
         f"...........................\n"

    )
      

    print(winning_candidate_summary)

    #save the winning candidate's name to the election results file
    with open("election_results.txt","a") as f:
        f.write(winning_candidate_summary)
    



    
     



