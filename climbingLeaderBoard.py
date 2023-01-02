'''
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
Example



The ranked players will have ranks , , , and , respectively. If the player's scores are ,  and , their rankings after each game are ,  and . Return .

Function Description

Complete the climbingLeaderboard function in the editor below.

climbingLeaderboard has the following parameter(s):

int ranked[n]: the leaderboard scores
int player[m]: the player's scores
Returns

int[m]: the player's rank after each new score


'''

#!/bin/python3

import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
  '''removing the duplicate'''
    ranked = list(set(ranked))
    ''' arrange from largest rank to smalles'''
    ranked.sort(reverse=True)
    rank = []
    for i in player:
        while len(ranked) > 0 and i >= ranked[-1]:
            ranked.pop()
        rank.append(len(ranked) + 1)
    return rank
    
'''

using binar search
def binary_search(arr, target):
    # Use binary search to find the rank of the target score
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid + 1
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
    return left + 1
I hope this helps! Let me know if you have any questions.






'''
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
