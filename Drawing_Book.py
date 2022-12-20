#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    n = (n + 1) if n % 2 == 0 else n
    p = (p + 1) if p % 2 == 0 else p
    x = [int((p - 1)/2), int((n - p)/2)]
    
    return min(x)
'''count_front=0
    count_back=0
    
    front_difference=p-0
    back_difference=n-p
    
    if front_difference <= back_difference:
        count_front=front_difference//2
        result=count_front
        
    else:
        if n % 2 !=0:
            count_back=(back_difference//2)
            result= count_back
        else:
            count_back=(back_difference//2)-1
            result=count_back
        
    return result'''
    #opening from front 
'''for i in range(0, n):
        if i<=p:
            
            count_front+=1
            count_front_num=(count_front//2)
       
    #opening from back
    for k in range(n, 0, -1):
        if k >=p:
            count_back+=1
            #pages even or odd
            if n%2!=0:
                count_back_num=(count_back//2)-1
            else:
                count_back_num=(count_back//2)
            
    if count_back_num < count_front_num:
        results=count_back_num
    elif count_back_num > count_front_num:
        results=count_front_num
    else:
        results=count_front_num
            
    return results'''
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
