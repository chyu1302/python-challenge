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
    Total_votes = len(data) -1
print(Total_votes)

with open(PyPoll_csv, "r") as f:
    csvreader=csv.reader(f, delimiter=",")
    next(csvreader)
    data = numpy.array(list(csvreader))
    candidates_received_votes= []
    names_list=set(data[:,2])
    print(names_list)
#    print(names_list)
#    csvreader= list(csvreader)
#    names_list.sort()
#    print(names_list)
#for i in range(3,len(data)):
#    if i+2 !=i+1:
#        print(data[i][1])
#        list.append(csvreader[i][3])
#        print(names_list)
    # for name in set(names):
#print("name '{}' appears {} unique times".format(name, names.count(name))
    
    #for i in range(2,len(csvreader)):
        #changes.append(int(csvreader[i][1])-int(csvreader[i-1][1]))
    #The average of the changes in "Profit/Losses" over the entire period    
#average=sum(changes)/len(changes) 
    #sort the list of changes
#changes.sort(reverse=False)
    #print greatest increase in profit
#print(changes[0])