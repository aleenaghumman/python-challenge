import csv
from math import *
with open('pypoll.csv') as r:
    string = csv.reader(r,delimiter=',')
    next(string)
    totalvoters = 0 # initialize voter count
    candidates = {} # inintialize dictionary of candidates, votes
    for row in string:
        totalvoters += 1 # add a voter to total count for every row in csv file
        if row[2] in candidates: # if a candidate's name is in the dictionary already,
            candidates[row[2]] += 1 # add a vote to their count
        else: # or else
            candidates[row[2]] = 1 # add the candidate to the dictionary
    candidatelist = [candidates.keys()] # making a list of candidate names
    candidatevotes = [candidates.values()] # turns candidate votes into a lsit
    maxvotes = max(candidatevotes) # find max number of votes in list of vote counts (variable candidatevotes)
    winner = candidatelist[candidatevotes.index(maxvotes)] # the corresponding index in the candidatelist is the winner
    print("Election Results")
    print("---------------------------------")
    print("Total Votes: {}".format(totalvoters))
    print("---------------------------------")
    for candidate in candidates:
        print("{}: {}% ({})".format(candidate,round(candidates[candidate]/totalvoters*100,3),candidates[candidate]))
    print("---------------------------------")
    print("Winner: {}".format(winner))
    print("---------------------------------")

