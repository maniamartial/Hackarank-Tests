'''
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return .

Example



The person can buy a , or a . Choose the latter as the more expensive option and return .

Function Description

Complete the getMoneySpent function in the editor below.

getMoneySpent has the following parameter(s):

int keyboards[n]: the keyboard prices
int drives[m]: the drive prices
int b: the budget
Returns

int: the maximum that can be spent, or  if it is not possible to buy both items
'''

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    store=[]
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    for k in keyboards:
        for d in drives:
            results= k+d
            if results <= b:
                store.append(results)
    if len(store)>=1:
        get_max=max(store)
    else:
        get_max=-1
    return get_max
    
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
