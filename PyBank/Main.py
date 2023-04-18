#import the csv
import csv

#creates file path across operating systems
import os

csvpath = os.path.join("Resources", "budget_data.csv")

#Open and Read file using csv module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
	#read the Header row first
    csvheader = next(csvreader)	
    
	#create empty lists to add the csv values to 
    month_count = []
    profit = []
    change_profit = []
    
                      
    #iterate through the values and add them to the empty list 
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      
#Calculate the min and max 
increase = max(change_profit)
decrease = min(change_profit)

#Locate the index value of max and min
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

#Print the analysis results to git bash terminal
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")      

#Export a text file with analysis results
analysis = os.path.join("Analysis", "financial_analysis")
with open(analysis,"w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("------------------------")
    txt_file.write("\n")
    txt_file.write(f"Total Months:{len(month_count)}")
    txt_file.write("\n")
    txt_file.write(f"Total: ${sum(profit)}")
    txt_file.write("\n")
    txt_file.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")