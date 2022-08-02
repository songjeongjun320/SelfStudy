"""
Given a non-negative integer x, compute and return the square
root of x.

Since the return type is an integer, the decimal digits are
truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function
or operator, such as pow(x,0.5) or x ** 0.5.
"""

class Solution():
    def mySqrt(self, x):
        _ = 0
        left = 0
        right = 0
        while True:
            left = _*_
            right = (_+1)*(_+1)
            if x >= left and x < right:
                return _
            _ += 1
    
testcase = Solution()
x = 0
print(testcase.mySqrt(x))