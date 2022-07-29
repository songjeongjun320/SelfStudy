class Solution(object):
    def removeDuplicates(self, nums):
        x = 1
        for _ in range(len(nums)-1):
            if nums[_] != nums[_+1]:
                nums[x] = nums[_+1]
                x+=1
        return x
testcase = Solution()

list_case = [0,0,1,1,1,2,2,3,3,4]
print(testcase.removeDuplicates(list_case))

# x = 1
# for i in range(len(nums)-1):
# 	if(nums[i]!=nums[i+1]):
# 		nums[x] = nums[i+1]
# 		x+=1
# return(x)