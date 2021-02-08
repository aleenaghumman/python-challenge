import csv 
from math import * # imports the math function (from mahnoors prior knowledge)
with open('dataset.csv') as r:
    string = csv.reader(r, delimiter = ',')
    next(string)
    months = 0 # defining the variables
    total = 0
    each = []
    rows = []
    for row in string:
        months += 1
        each.append(int(row[1])) # putting months into a list (from zybooks)
        total += int(row[1]) 
        rows.append(row[0]) # putting rows into a list (from zybooks)
    profitlosses = 0 #setting the profitlosses
    changes = []
    for i in range(0,len(each)-1):
        changes.append(each[i+1] - each[i]) #adds difference of amounts to list
        
    print('Financial Analysis')
    print('------------------------------')
    print('Total Months:', months)
    print('Total:',total)
    print('Average Change:',sum(changes) / len(changes))
    
    
        
decrease = changes.index(max(changes))
greatest_decrease = rows[decrease+1]
print ('Greatest decrease in profits: {} ({})'.format(rows[decrease+1],min(changes)))

increase = changes.index(min(changes))
greatest_increase = rows[increase+1]
print ('Greatest increase in profits: {} ({})'.format(rows[increase+1],max(changes)))
