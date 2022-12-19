'''
Marie invented a Time Machine and wants to test it by time-traveling to visit Russia on the Day of the Programmer (the 256th day of the year) during a year in the inclusive range from 1700 to 2700.

From 1700 to 1917, Russia's official calendar was the Julian calendar; since 1919 they used the Gregorian calendar system. The transition from the Julian to Gregorian calendar system occurred in 1918, when the next day after January 31st was February 14th. This means that in 1918, February 14th was the 32nd day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of days; it has 29 days during a leap year, and 28 days during all other years. In the Julian calendar, leap years are divisible by 4; in the Gregorian calendar, leap years are either of the following:

Divisible by 400.
Divisible by 4 and not divisible by 100.
Given a year, , find the date of the 256th day of that year according to the official Russian calendar during that year. Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is .

For example, the given  = 1984. 1984 is divisible by 4, so it is a leap year. The 256th day of a leap year after 1918 is September 12, so the answer is .

Function Description

Complete the dayOfProgrammer function in the editor below. It should return a string representing the date of the 256th day of the year given.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if year < 1918 and ((year%4) == 0):
        return(f'12.09.{year}')
    elif year == 1918:
        return(f'26.09.{year}')
    elif (year%400 == 0) or (year%4 == 0 and year%100 != 0):
        print('leap')
        return(f'12.09.{year}')
    else:
        return(f'13.09.{year}')
    '''jan=31
    march=31
    april=30
    may=31
    june=30
    july=31
    aug=31
    sep=30
    
    if year < 1918:
        if year % 4==0 :
            feb=29
        else:
            feb=28
    
    if year > 1918:
        if year %400==0 or (year%4==0 and year%100!=0):
            feb=29
        else:
            feb =28
            
    if year==1918:
        print("26.09.1918")
            
        
    
    first_month=jan+feb+march+april+may+june+july+aug
    sep_days=str(256-first_month)
    
    return sep_days+'.09.'+str(year)'''

       
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
