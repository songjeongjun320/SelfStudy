"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing
order, and two integers m and n, representing the number of elements in nums1
and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasong order.

The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accomodate this, nums1 has a length of
m + n, where the first m elements denote the elements that should be merged, and
the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution():
    def merge(self, nums1, m, nums2, n):
        for _ in range(len(nums2)):
            nums1.append(nums2[_])
        nums1.sort()
        while len(nums1) != m+n:
            nums1.remove(0)
        return nums1

nums1 = [-1,0,0,3,3,3,0,0,0]
nums2 = [1,2,2]
m = 6
n = 3

testcase = Solution()
print(testcase.merge(nums1,m,nums2,n))