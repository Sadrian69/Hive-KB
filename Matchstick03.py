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
# 6x7
stack.append(['D1', 'C1', 'B1', 'A1'])  #1
stack.append(['E1', 'E2', 'E3'])        #2
stack.append(['F1', 'F2'])              #3
stack.append(['D2', 'C2', 'B2'])        #4    
stack.append(['A3', 'A2'])              #5
stack.append(['B3', 'C3', 'D3'])        #6
stack.append(['F3', 'F4'])              #7
stack.append(['A4', 'B4'])              #8
stack.append(['E4', 'D3', 'C4'])        #9
stack.append(['G4', 'G3', 'G2'])        #10
stack.append(['A5', 'B5', 'C5', 'D5'])  #11
stack.append(['G5', 'G6'])              #12
stack.append(['C6', 'B6', 'A6'])        #13
stack.append(['E6', 'D6'])              #14
stack.append(['F6', 'F5'])              #15

rCounts = ([3,4,3,4,3,4,3])
cCounts = ([4,4,6,3,5,4])
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
    # puzzle yg tidak bisa di solve, nilai minimal objective function = 2


# ---- END
