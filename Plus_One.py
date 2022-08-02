"""
You are given a larger integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer. The digits are
ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution():
    def plusOne(self, digits):
        digits[len(digits)-1] += 1
        return digits
    
testcase = Solution()
digits = [1,2,3]

print(testcase.plusOne(digits))