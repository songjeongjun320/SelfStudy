"""
Given two strings needle and haystack, return the index of the first
occurence of needle in haystack, or -1 if needle is not part of haystack.

"""

class Solution(object):
    def strStr(self, haystack, needle):
        for _ in range(len(haystack)):
            if not needle in haystack:
                return -1
        return haystack.index(needle)

testcase = Solution()
haystack = "hello"
needle = "ll"

print(testcase.strStr(haystack,needle))
