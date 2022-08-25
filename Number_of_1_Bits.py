class Solution():
    def hammingWeight(self, n):
        n = str(n)
        nums = []
        print(len(n))
        for _ in range(len(n)):
            nums.append(int(n[_]))
        count = nums.count(1)
        return count
        
testcase = Solution()
n = 00000000000000000000000000001011
print(testcase.hammingWeight(n))