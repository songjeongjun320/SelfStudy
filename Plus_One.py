"""
You are given a larger integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer. The digits are
ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution():
    def plusOne(self, digits):
        digits.reverse()
        r = 1
        for _ in range(len(digits)):
            digits[_] = digits[_] + r
            r = 0
            if digits[_] == 10:
                digits[_] = 0
                r = 1
        if r == 1:
            digits.append(1)
        digits.reverse()
        return digits
    
testcase = Solution()
digits = [9]

print(testcase.plusOne(digits))

# 이거 리스트 위치에 따라서 10의 승수로 계산하기