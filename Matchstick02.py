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
# 5x10
stack.append(['F1', 'E1', 'D1', 'C1', 'B1', 'A1'])  #1
stack.append(['J1', 'I1', 'H1'])                    #2
stack.append(['A2', 'A3', 'A4', 'A5'])              #3
stack.append(['C2', 'D2', 'E2', 'F2'])              #4    
stack.append(['H2', 'H3', 'H4'])                    #5
stack.append(['J2', 'J3', 'J4'])                    #6
stack.append(['C3', 'C4', 'C5'])                    #7
stack.append(['F3', 'F4'])                          #8
stack.append(['E4', 'E3'])                          #9
stack.append(['G4', 'G3', 'G2', 'G1'])              #10
stack.append(['I4', 'I3', 'I2'])                    #11
stack.append(['B5', 'B4', 'B3', 'B2'])              #12
stack.append(['D5', 'D4', 'D3'])                    #13
stack.append(['J5', 'I5', 'H5', 'G5', 'F5', 'E5'])  #14

rCounts = ([2,2,2,5,2,2,2,3,3,4])
cCounts = ([5,5,7,5,5])
# jangan edit yang lain

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
    # print(evaluator([4,1,2,2,2,2,0,1,1,2,2,2,3,3]))


# ---- END
