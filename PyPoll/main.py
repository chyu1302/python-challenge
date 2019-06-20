# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:28:01 2019

@author: yuepe
"""
import os
import csv
import numpy

PyPoll_csv =os.path.join("..","Resources","election_data.csv")

with open(PyPoll_csv, "r") as f:
    csvreader=csv.reader(f, delimiter=",")
    
    data = list(csvreader)
    Total_votes = len(data)-1
print(Total_votes)

with open(PyPoll_csv, "r") as f:
    csvreader=csv.reader(f, delimiter=",")    
    next(csvreader)
    data = numpy.array(list(csvreader))
    unique, counts = numpy.unique(data[:,2], return_counts=True)
    #Find the winner
    winner = max(set(data[:,2]),key =list(data[:,2]).count)
    # Count votes for each candidate
    votes_each_candidate = list(zip(unique, counts))
    
    print("Election Results")
    print("-----------------")
    print(f'Total Votes:{Total_votes}')
    print("-----------------")
    print(f'{unique[0]}: {((counts[0]/Total_votes)*100):.3f}% ({counts[0]})')
    print(f'{unique[1]}: {((counts[1]/Total_votes)*100):.3f}% ({counts[1]})')
    print(f'{unique[2]}: {((counts[2]/Total_votes)*100):.3f}% ({counts[2]})')
    print(f'{unique[3]}: {((counts[3]/Total_votes)*100):.3f}% ({counts[3]})')
    print("-----------------")
    print(f'Winner:{winner}')
   