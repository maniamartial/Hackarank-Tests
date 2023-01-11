'''

A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. The character must jump from cloud to cloud until it reaches the start again.

There is an array of clouds,  and an energy level . The character starts from  and uses  unit of energy to make a jump of size  to cloud . If it lands on a thundercloud, , its energy () decreases by  additional units. The game ends when the character lands back on cloud .

Given the values of , , and the configuration of the clouds as an array , determine the final value of  after the game ends.

Example. 

The indices of the path are . The energy level reduces by  for each jump to . The character landed on one thunderhead at an additional cost of  energy units. The final energy level is .

Note: Recall that  refers to the modulo operation. In this case, it serves to make the route circular. If the character is at  and jumps , it will arrive at .

Function Description

Complete the jumpingOnClouds function in the editor below.

jumpingOnClouds has the following parameter(s):

int c[n]: the cloud types along the path
int k: the length of one jump
Returns

int: the energy level remaining.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100
    i = 0
    n = len(c)
    while i != 0 or energy == 100:
        i = (i + k) % n
        energy -= 1 + c[i] * 2
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
 
