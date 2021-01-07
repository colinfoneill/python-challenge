# import dependencies
import csv
import os

# establish file path for csv file
election_data_path = os.path.join("Resources", "election_data.csv")

# open the file for reading
with open(election_data_path, 'r') as csvfile:
    # read the file, specify a delimiter, and store the contents in a variable
    csv_reader = csv.reader(csvfile, delimiter = ",")
    # skip the header row
    csv_header = next(csv_reader)

    # initialize voter count to 0
    voter_count = 0

    # initialize blank candidate:votes dictionary
    candidate_votes = {}
    
    # loop through each row in the csv file
    for row in csv_reader:
        # count the # of voters
        voter_count += 1

        # add votes for each candidate as you loop through the rows in the csv file
        candidate = row[2] 
        if candidate in candidate_votes.keys():
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1
   
    # create empty lists for candidate and vote count
    candidates = []
    votes = []

    # extract the key and value from the candidate_votes dictionary and place each into the respective list
    for key, value in candidate_votes.items():
        candidates.append(key)
        votes.append(value)

    # calculate each candidates % of votes won and put into a list
    vote_percentage = []
    for vote in votes:
        vote_percentage.append(round((vote/voter_count)*100, 1))

    # zip lists together and convert into one list
    cleaned_csv = list(zip(candidates, votes, vote_percentage))

    # find and create list of winner
    winner_list = []
    for candidate in cleaned_csv:
        if max(votes) == candidate[1]:
            winner_list.append(candidate[0])
    
    # convert winner list to a string
    winner = str(winner_list[0])
          
       
    # print results to terminal
    print("Election Results")
    print('----------------------------')
    print(f'Total Votes: {voter_count}')
    print("----------------------------")
    for c in range(len(candidates)):
        print(f'{candidates[c]}: {str(vote_percentage[c])}% ({str(votes[c])})')
    print("----------------------------")
    print(f'Winner: {winner}')
    print("----------------------------")

# write results to output csv file
output_path = os.path.join("Analysis", "poll_results.txt")

with open(output_path, "w") as csvwritefile:
    csvwriter = csv.writer(csvwritefile, delimiter = ",")

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow([f'Total Votes: {voter_count}'])
    csvwriter.writerow(["----------------------------"])
    for c in range(len(candidates)):
        csvwriter.writerow([f'{candidates[c]}: {str(vote_percentage[c])}% ({str(votes[c])})'])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f'Winner: {winner}'])
    csvwriter.writerow(["----------------------------"])
