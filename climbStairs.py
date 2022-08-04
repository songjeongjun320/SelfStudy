"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct
ways can you climb to the top?
"""

class Solution():
    def climbStairs(self, n):
        if n == 1:
            return 1
        
        tmp = []
        top = 1
        left = 1
        right = 1
        count = 0
        for x in range(n+1):
            y = int((n-x)/2)
            if n == x + 2*y:
                tmp.append([x,y])
        print(tmp)
        for _ in range(len(tmp)):
            if tmp[_][0] != 0 and tmp[_][1] != 0:
                for i in range(1,tmp[_][0]+tmp[_][1]+1):
                    top *= i
                for i in range(1, tmp[_][0]+1):
                    left *= i
                for i in range(1, tmp[_][1]+1):
                    right *= i
            if tmp[_][0] == 0 or tmp[_][1] == 0:
                count += 1
        
        count += int(top/(left*right))
        return count
    
testcase = Solution()
n = 2
print(testcase.climbStairs(n))