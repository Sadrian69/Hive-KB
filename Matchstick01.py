#!/usr/bin/env python

# ---- IMPORT MODULES

import math

try:
    import numpy as np
except:
    raise ImportError("Numpy module not installed.")

from Hive import Utilities
from Hive import Hive

# ---- CREATE TEST CASE

stack = []

# edit yang ini
stack.append(['B6', 'C6', 'D6', 'E6', 'F6'])  
stack.append(['B5', 'B4', 'B3', 'B2'])        
stack.append(['F5', 'E5', 'D5', 'C5'])        
stack.append(['C4', 'C3'])                    
stack.append(['D4', 'E4'])                    
stack.append(['F4', 'F3', 'F2'])              
stack.append(['A3', 'A4', 'A5', 'A6'])        
stack.append(['E3', 'D3'])                    
stack.append(['A2', 'A1'])                    
stack.append(['C2', 'D2', 'E2'])              
stack.append(['F1', 'E1', 'D1', 'C1', 'B1'])  

rCounts = ([3,4,2,3,4,3])
cCounts = ([3,3,3,4,3,3])
# jangan edit yang lain

# Meike buat ini buat nge-passing ke GUI
new_stack = []
for sublist in stack:
    if sublist:  # Cek sublist gak kosong
        first_value = sublist[0]
        last_value = sublist[-1]
        new_stack.append((first_value, last_value))

stackArray = []
lowerBound = []
upperBound = []

for t, envRow in enumerate(stack):
    row = []
    
    for envCell in envRow:
        cell = []
        # Break the A, B, C, etc to 0,1,2 so it is easier to process
        cell.append(ord(envCell[0]) - ord('A'))
        # Convert chars 1,2,3 into 0,1,3
        cell.append(ord(envCell[1]) - ord('1'))
        # Now save this cell config
        row.append(cell)
    
    stackArray.append(row)
    
    lowerBound.append(0)
    upperBound.append(len(row))

stackCounts = []
stackCounts.append(rCounts)
stackCounts.append(cCounts)


def evaluator(vector):
    fsCount = [[],[]]
    fsCount[0] = [0] * len(stackCounts[0])
    fsCount[1] = [0] * len(stackCounts[1])
    
    for match,burn in enumerate(vector):
        for i in range(int(burn)):
            fsCount[0][stackArray[match][int(i)][0]] += 1
            fsCount[1][stackArray[match][int(i)][1]] += 1

    fnValue = 0
    for dim in range(2):
        for rcNum in range(len(fsCount[dim])):
            fnValue += pow(stackCounts[dim][rcNum] - fsCount[dim][rcNum],2)
    
    return fnValue        

# ---- SOLVE TEST CASE WITH ARTIFICIAL BEE COLONY ALGORITHM

def run():

    # creates model
    model = Hive.BeeHive(lower     = lowerBound ,
                         upper     = upperBound ,
                         fun       = evaluator  ,
                         numb_bees =  80        ,
                         max_itrs  =  200       ,)

    # runs model
    cost, solution = model.run()

    # plots convergence
    # Utilities.ConvergencePlot(cost)

    # prints out best solution
    print("Fitness Value ABC: {0}".format(model.best))
    print(solution)
    


if __name__ == "__main__":
    run()
    # print(evaluator([3,3,2,0,2,1,1,1,2,2,2]))


# ---- END
