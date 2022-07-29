"""
Given a astring s, find the length of the longest
substring without repeating characters
"""

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        if not s:
            return 0
        count = 1
        tmp_list = []
        for j in range(len(s)):
            if not s[j] in tmp_list:
                tmp_list.append(s[j])
            else:
                count = max(count,len(tmp_list))
                tmp_list = []
                j = s.index(s[j])+1
            count = max(count,len(tmp_list))

        return count
                    
        
        
                
testcase = Solution()

input = "ababcb"
print(testcase.lengthOfLongestSubstring(input))