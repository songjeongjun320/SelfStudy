"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.
"""

nums = [3,2,4]
switch = True
output = []
sum = 0
target = 6

for i in range(len(nums)):
    if switch == False:
        break
    for j in range(len(nums)):
        if i == j:
            continue
        else:
            if nums[i] + nums[j] == target:
                output.append(i)
                output.append(j)
                switch = False
                break

print(output)
