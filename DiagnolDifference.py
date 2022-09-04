
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n=len(arr)                            
    firstdiagnol=sum(arr[i][i] for i in range(n))
    lastdiagnol=sum(arr[i][(n-1)-i] for i in range(n))
    
    return abs(firstdiagnol - lastdiagnol)
    '''d=0
    l=len(arr)
    for i in range(l):
        d+=(arr[i][i] - arr[l-i-1][i])
        if(d>=0):
            return d
        return -d'''
        
        
            
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()