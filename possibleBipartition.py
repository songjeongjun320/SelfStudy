""" 
We want to split a group of n people
(labeled from 1 to n) into two groups of any size.
Each person may dislike some other people, and they
should not go into the same group.

Given the integer n and the array dislikes where
dislikes[i] = [ai, bi] indicates that the person labeled
ai doesn't like the person labeled bi, return true
if it is possible to split everyone into two groups in this way.
"""

n = 4
dislikes = [[1,2],[1,3],[2,4]]

total_num = 0

for _ in range(1, n):
    total_num += _
    
print(total_num)

