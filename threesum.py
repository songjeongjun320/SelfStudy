"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""

# nums = [-1,0,1,-1]
# list_size = len(nums)*(len(nums)-1)*(len(nums)-2)
# sum = 0 # 삼중 포문 안에서 더하는 값을 저장할 변수 / 마지막에는 target이 되는 변수
# count = 0 # 몇번째인지 숫자를 셀 변수

# two_d_list = [[0 for _ in range(4)] for _ in range(list_size)] # i j k 의 값을 저장할 리스트

# ## 제시된 nums의 모든 three sum 경우의 수 판별, 그 중 중복된 sum값 찾아냄.
# for i in range(len(nums)):
#     sum = nums[i]
#     for j in range(len(nums)):
#         if i == j:
#             pass
#         else:
#             sum = sum + nums[j]
#             for k in range(len(nums)):
#                 if i == k or j == k:
#                     pass
#                 else:
#                     sum = sum + nums[k]
#                     two_d_list[count][0] = nums[i]
#                     two_d_list[count][1] = nums[j]
#                     two_d_list[count][2] = nums[k]
#                     two_d_list[count][3] = sum
#                     count += 1
#                     print(two_d_list)
#                     print()
#                     sum = sum - nums[k]
#             sum = sum - nums[j]

# # target 값이 0인 리스트 도출
# case = 0
# s = set()
# for _ in range(count):
#     if two_d_list[_][3] == 0:
#         tmp = []
#         tmp.append(two_d_list[_][0])
#         tmp.append(two_d_list[_][1])
#         tmp.append(two_d_list[_][2])
#         tmp.sort()
#         s.add(tuple(tmp))
#         case += 1

# output = [[0 for _ in range(4)] for _ in range(len(s))]
# for _ in range(len(s)):
#     tmp = s.pop()
#     list_tmp = []
#     list_tmp = list(tmp)
#     print(tmp)
#     output[_] = list_tmp

# print(output)


nums = [-1,0,1,-1]
list_size = len(nums)*(len(nums)-1)*(len(nums)-2)
sum = 0 # 삼중 포문 안에서 더하는 값을 저장할 변수 / 마지막에는 target이 되는 변수
count = 0 # 몇번째인지 숫자를 셀 변수

two_d_list = [[0 for _ in range(4)] for _ in range(list_size)] # i j k 의 값을 저장할 리스트

## 제시된 nums의 모든 three sum 경우의 수 판별, 그 중 중복된 sum값 찾아냄.
for i in range(len(nums)):
    sum = nums[i]
    for j in range(len(nums)):
        if i == j:
            pass
        else:
            sum = sum + nums[j]
            for k in range(len(nums)):
                if i == k or j == k:
                    pass
                else:
                    sum = sum + nums[k]
                    two_d_list[count][0] = nums[i]
                    two_d_list[count][1] = nums[j]
                    two_d_list[count][2] = nums[k]
                    two_d_list[count][3] = sum
                    count += 1
                    sum = sum - nums[k]
            sum = sum - nums[j]

# target 값이 0인 리스트 도출
case = 0
s = set()
for _ in range(count):
    if two_d_list[_][3] == 0:
        tmp = []
        tmp.append(two_d_list[_][1])
        tmp.append(two_d_list[_][2])
        tmp.sort()
        s.add(tuple(tmp))
        case += 1

output = [[0 for _ in range(4)] for _ in range(len(s))]
for _ in range(len(s)):
    tmp = s.pop()
    output[_] = tmp
print(output)