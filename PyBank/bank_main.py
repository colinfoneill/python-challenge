# import dependencies 
import os
import csv

# store the path associated with the csv file
budget_data_path = os.path.join("Resources", "budget_data.csv")

# open the file in read mode and store the contents in a variable
with open(budget_data_path, 'r') as csvfile:
    # read the file, specify a delimiter, and store the contents in a variable
    csv_reader = csv.reader(csvfile, delimiter = ',')
    # skip the header row  
    next(csv_reader)
        
    # initialize total_months variable to 0
    total_months = 0

    #initialize profit_loss variable to 0
    profit_loss = 0
    
    # create empty list for months and monthly profit
    months = []
    monthly_profit = []

    
    # loop through each row of the csv file 
    for row in csv_reader:
        # add 1 to total months count
        total_months += 1

        #aggregate the profit/loss for each month and store in variable
        profit_loss = profit_loss + int(row[1])

        #create lists of months and monthly profit as we loop through csv file
        months.append(row[0])
        monthly_profit.append(row[1])
    #initialize change_profit_list to blank
    change_profit_list = []
    
    #loop through dates and profits and calculate the month over month change in profit
    for i in range(1, len(months)):
        change_profit = int(monthly_profit[i]) - int(monthly_profit[i-1])
        change_profit_list.append(change_profit)
    
    # calculcate average of values in the change_profit_list
    average_change_profit = round(sum(change_profit_list)/len(change_profit_list), 2)
    
    # find the max and min changes in profit
    max_profit = max(change_profit_list) 
    min_profit = min(change_profit_list)

    # loop through change_profit_list to find max profit and its corresponding date
    for profit in range(len(change_profit_list)):
        date_index = change_profit_list.index(max_profit)
        date_max = months[date_index + 1]

    # loop through change_profit_list to find min profit and its corresponding date
    for profit in range(len(change_profit_list)):
        date_index = change_profit_list.index(min_profit)
        date_min = months[date_index + 1]
        
       
    # print outputs
    print("Financial Analysis")
    print("-------------------")
    print(f'Total Months: {total_months}')
    print(f'Total Profit(Loss): ${profit_loss}')
    print(f'Average Monthly Change in Profit(Loss): ${average_change_profit}')
    print(f'Greatest Increase in Profits: {date_max} (${max_profit})')
    print(f'Greatest Decrease in Profits: {date_min} (${min_profit})')

    # export results to a text file
output_path = os.path.join("Analysis", "bank_results.txt")

    #open the file using write mode and specify the variable to hold the contents
with open(output_path, "w") as csvwritefile:

    # initialize csv writer
    csvwriter = csv.writer(csvwritefile, delimiter = ",")

    # write the results
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow([f'Total Months: {total_months}'])
    csvwriter.writerow([f'Total Profit(Loss): ${profit_loss}'])
    csvwriter.writerow([f'Average Monthly Change in Profit(Loss): ${average_change_profit}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {date_max} (${max_profit})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {date_min} (${min_profit})'])
