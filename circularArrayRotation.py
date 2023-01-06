'''
John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position and shifts all remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

For each array, perform a number of right circular rotations and return the values of the elements at the given indices.

Example

Here  is the number of rotations on , and  holds the list of indices to report. First we perform the two rotations: 

Now return the values from the zero-based indices  and  as indicated in the  array.


Function Description

Complete the circularArrayRotation function in the editor below.

circularArrayRotation has the following parameter(s):

int a[n]: the array to rotate
int k: the rotation count
int queries[1]: the indices to report
Returns

int[q]: the values in the rotated  as requested in 

'''

#!/bin/python3

import math
import os
import random
import re
import sys

def circularArrayRotation(a, k, queries):
    #this was my original code that failed ony one test
    '''new_array=[]
    for i in range(k):
        #getting the last element
        last_element=a[-1]
        #removing the last element
        a=a[:-1]
        a.insert(0, last_element)
    #for i, element in enumerate(a):
    return [a[q] for q in queries]'''
    for i in range(k):
        a.insert(0,a.pop())
    return [a[q] for q in queries]

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
