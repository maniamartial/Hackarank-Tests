'''
Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def migratoryBirds(arr):
     counter = Counter(arr)
     
     #lets get the value with maximum number of repetation
     max_value=max(counter.values())
     
     #lets the get the smallest value but with max number of frequesncy
     min_value=min([k for k, v in counter.items() if v ==max_value])
     return min_value
     
                
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
