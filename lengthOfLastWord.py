class Solution():
    def lengthOfLastWord(self, s):
        s = s.strip()
        count = 0
        for _ in range(len(s)):
            if s[_] == " ":
                count = 0
            else:
                count += 1
        return count
    
testcase = Solution()
s = "    fly me to the moon  "

print(testcase.lengthOfLastWord(s))