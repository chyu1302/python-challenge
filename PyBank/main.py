# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:27:22 2019

@author: yuepe
"""
import os
import csv
PyBank_csv =os.path.join("..","Resources","PyBank_budget_data.csv")

with open(PyBank_csv, "r") as f:
    csvreader=csv.reader(f, delimiter=",")
    data = list(csvreader)
    row_count = len(data) -1
print(row_count)

with open(PyBank_csv, "r") as f:
    csvreader=csv.reader(f, delimiter=",")
    next(csvreader)
    total = sum(int(line[1]) for line in csvreader)
    
print(total)
with open(PyBank_csv,"r") as f:
    csvreader=csv.reader(f, delimiter=",")
    changes=[]
    csvreader= list(csvreader)
    for i in range(2,len(csvreader)):
        changes.append(int(csvreader[i][1])-int(csvreader[i-1][1]))
    #The average of the changes in "Profit/Losses" over the entire period    
average=sum(changes)/len(changes) 
    #sort the list of changes
changes.sort(reverse=False)
    #print greatest increase in profit
print(changes[0])
    #print greatest decrease in profit
print(changes[84])
    #average change
print(average)
with open("PyBank_report.txt","w") as report:
    report.write(f'Financial Analysis\n')
    report.write(f'----------------------------\n')
    report.write(f'Total Months: {total}\n')
    report.write(f'Average Change:{average}\n')
    report.write(f'Greatest Increase in Profits:{changes[84]}\n')
    report.write(f'Greatest Decrease in Profits:{changes[0]}\n')

    
    