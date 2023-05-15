#Dependancies
import os
import csv

budget_csv= os.path.join("..","Resources", "budget_data.csv")


#Profit/losses analysis parameters
total_months=0
prev_profit_losses=0
month_of_change=[]
profit_losses_change_list=[]
greatest_increase=["",0]
greatest_decrease=["",99999999999999]
total_profit_losses=0



# Open and read csv and convert it into list of dictionaries
with open(budget_csv) as profit_losses_data:
    reader = csv.DictReader(profit_losses_data)
 
 #Read through row of data

    for row in reader:

        #Calculate the total number of months

        total_months=total_months+1

        #Calculate the profit or losses over the entire period
        total_profit_losses=total_profit_losses + int(row["Profit/Losses"])

        #Calculate the changes in profit/losses
        profit_losses_change=int(row["Profit/Losses"])-prev_profit_losses
        prev_profit_losses=int(row["Profit/Losses"])
        profit_losses_change_list=profit_losses_change_list + [profit_losses_change]
        month_of_change=month_of_change+[row["Date"]]
        
        #Calculate the greatest increase in profit

        if (profit_losses_change > greatest_increase [1]):
            greatest_increase[0]=row["Date"]
            greatest_increase[1]=profit_losses_change

        #Calculate the greatest decrease

        if (profit_losses_change<greatest_decrease[1]):
            greatest_decrease[0]=row["Date"]
            greatest_decrease[1]=profit_losses_change

#Calculate the average profit or losses change

profit_losses_avg=sum(profit_losses_change_list) / len(profit_losses_change_list)

#Generate output Summary
output = (
    f"\nFinancial Analysis\n"

    f"----------------------------\n"

    f"Total Months: {total_months}\n"

    f"Total Profit/losses: ${total_profit_losses}\n"

    f"Average profit/losses Change: ${profit_losses_avg}\n"

    f"Greatest Increase in profit/losses: {greatest_increase[0]} (${greatest_increase[1]})\n"
    
    f"Greatest Decrease in profit/losses: {greatest_decrease[0]} (${greatest_decrease[1]})\n"

)
#Set variable for output file

output_file=os.path.join("..","Analysis","output.txt")

# Print the output
print(output)

# Export the results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)


    
        











