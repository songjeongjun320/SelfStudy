"""
Given a astring s, find the length of the longest
substring without repeating characters
"""

# Time Limitation

# class Solution(object):
#     def lengthOfLongestSubstring(self,s):
#         if not s:
#             return 0
#         count = 1
#         for _ in range(len(s)):
#             tmp_list = []
#             for j in range(_,len(s)):
#                 if not s[j] in tmp_list:
#                     tmp_list.append(s[j])
#                 else:
#                     count = max(count,len(tmp_list))
#                     tmp_list = []
#             count = max(count,len(tmp_list))

#         return count

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        if s == " ":
            return 1
        output_list = []
        output = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in output_list:
                output_list.append(s[r])
                output = max(output, r - l + 1)
            else:
                output = max(output, r - l)
                output_list.clear()
                l = l + 1
                r = l
                continue
            r += 1                    
                              
        return output        

testcase = Solution()

input = "abcabcbb"
print(testcase.lengthOfLongestSubstring(input))