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
n = format(11,'b')
print(n)
print(testcase.hammingWeight(n))