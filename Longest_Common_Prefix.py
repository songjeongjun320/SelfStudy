""" 
Write a function to find the longest common prefix
string amongst an array of strings.

If there is no common prefix, return an empty string"".
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs)
        print(shortest)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 

test = Solution()


strs = ["flower", "flow", "flight"]
print(test.longestCommonPrefix(strs))

strs_1 = []
print(test.longestCommonPrefix(strs_1))

strs_2 = ["a"]
print(test.longestCommonPrefix(strs_2))

strs_3 = ["ab", "a"]
print(test.longestCommonPrefix(strs_3))