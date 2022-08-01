"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""

class Solution():
    def searchInsert(self, nums, target):
        for _ in range(len(nums)):
            if target <= nums[_]:
                return _
        return len(nums)
    
testcase = Solution()

target = 7
nums = [1,3,5,6]

print(testcase.searchInsert(nums,target))