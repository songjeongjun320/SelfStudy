"""
Given an integer x, return true if x is palindrome integer.
    
An integer is a palindrome when it reads the same
backward as forward.

"""

from numpy import True_


x = 121
x = str(x)
left = 0
right = len(x)-1
switch = True

while left < right:
    if x[left] != x[right]:
        switch = False
        break
    left += 1
    right -= 1

if switch == True:
    print(True)
else:
    print(False)