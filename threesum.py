"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""

nums = [14,4,6,-1,10,9,-8,7,-13,14,-13,-11,-8,-9,11,14,-8,-14,-13,7,-10,-15,-13,-11,-11,11,14,13,2,-14,1,-7,-2,14,-1,-15,9,7,-1,3,6,1,7,5,-1,-5,4,-2,-4,-1,-9,-7,-1,-7,-11,3,12,10,-7,-1,12,1,8,-13,1,14,9,-13,6,-7,-3,-11,2,-11,10,-14,-1,-9,0,2,5,6,3,-11,6,7,0,3,3,0,-12,-8,-13,3,-14,-5,2,10,-11,-14,-12,1,-10,5,5,7,-1,11,14,6,-10,-4,-3,8,-7,10,1,8,-1,-11,-15,-6,-12,-13,12,-11]
# nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]

nums.sort()
sum = 0 # 삼중 포문 안에서 더하는 값을 저장할 변수 / 마지막에는 target이 되는 변수
output = []
s = set()

## 제시된 nums의 모든 three sum 경우의 수 판별, 그 중 중복된 sum값 찾아냄.
for i in range(len(nums)):
    if i+1 < len(nums) and nums[i] == nums[i+1]:
        continue
    sum = nums[i]
    for j in range(len(nums)):
        if i!= j:
            sum = sum + nums[j]
            for k in range(len(nums)):
                if i == k or j == k:
                    continue
                else:
                    sum = sum + nums[k]
                    
                    # target 값이 0인 리스트 도출
                    if sum == 0:
                        tmp = []
                        tmp.append(nums[i])
                        tmp.append(nums[j])
                        tmp.append(nums[k])
                        tmp.sort()
                        if tuple(tmp) not in s:
                            s.add(tuple(tmp))
                            output.append(tmp)
                    
                    sum = sum - nums[k]
            sum = sum - nums[j]
print(output)

"""
More Fastest version

nums = [14,4,6,-1,10,9,-8,7,-13,14,-13,-11,-8,-9,11,14,-8,-14,-13,7,-10,-15,-13,-11,-11,11,14,13,2,-14,1,-7,-2,14,-1,-15,9,7,-1,3,6,1,7,5,-1,-5,4,-2,-4,-1,-9,-7,-1,-7,-11,3,12,10,-7,-1,12,1,8,-13,1,14,9,-13,6,-7,-3,-11,2,-11,10,-14,-1,-9,0,2,5,6,3,-11,6,7,0,3,3,0,-12,-8,-13,3,-14,-5,2,10,-11,-14,-12,1,-10,5,5,7,-1,11,14,6,-10,-4,-3,8,-7,10,1,8,-1,-11,-15,-6,-12,-13,12,-11]
# nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]

nums.sort()
sum = 0 # 삼중 포문 안에서 더하는 값을 저장할 변수 / 마지막에는 target이 되는 변수
output = []
s = set()

## 제시된 nums의 모든 three sum 경우의 수 판별, 그 중 중복된 sum값 찾아냄.
for i in range(len(nums)):
    if i+1 >= len(nums):
        continue
    sum = nums[i]
    j = i+1
    k = len(nums)-1
    while j < k:
        sum = nums[i] + nums[j] + nums[k]
        if sum == 0:
            tmp = []
            tmp.append(nums[i])
            tmp.append(nums[j])
            tmp.append(nums[k])
            tmp.sort()
            if tuple(tmp) not in s:
                s.add(tuple(tmp))
                output.append(tmp)
            j += 1
        elif sum < 0:
            j += 1
        elif sum > 0:
            k -= 1   

print(output)
"""