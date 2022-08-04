"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct
ways can you climb to the top?
"""

from math import factorial


class Solution():
    def climbStairs(self, n):
        if n == 1:
            return 1
        tmp = []
        count = 0
        for x in range(n+1):
            y = int((n-x)/2)
            if n == x + 2*y:
                tmp.append([x,y])
        print(tmp)
        for _ in range(len(tmp)):
            count += int(factorial(tmp[_][0]+tmp[_][1])/(factorial(tmp[_][0])*factorial(tmp[_][1])))
        return count
    
testcase = Solution()
n = 3
print(testcase.climbStairs(n))
