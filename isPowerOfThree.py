class Solution:
    def isPowerOfThree(self, n):
        while n > 1:
            n /= 3
        if n == 1:
            return True
        else:
            return False