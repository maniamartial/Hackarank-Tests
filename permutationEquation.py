'''

Given a sequence of  integers,  where each element is distinct and satisfies . For each  where , that is  increments from  to , find any integer  such that  and keep a history of the values of  in a return array.

Example


Each value of  between  and , the length of the sequence, is analyzed as follows:

, so 
, so 
, so 
, so 
, so 
The values for  are .

Function Description

Complete the permutationEquation function in the editor below.

permutationEquation has the following parameter(s):

int p[n]: an array of integers
Returns

int[n]: the values of  for all  in the arithmetic sequence  to 
'''

def permutationEquation(p):
    # Write your code here
    result=[]
    for x in range(1,len(p)+1):
        result.append(p.index(p.index(x)+1)+1)
    return result
