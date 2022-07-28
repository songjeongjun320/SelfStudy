"""
Given two strings s and t, return true if t is an anagram of s, and false other wise.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.

"""

class Solution(object):
    def isAnagram(self, s, t):
        list_s = []
        list_t = []
        if len(s) != len(t):
            return False
        for _ in range(len(s)):
            list_s.append(s[_])
            list_t.append(t[_])
        list_s.sort()
        list_t.sort()
        if list_s == list_t:
            return True
        else:
            return False
    
testcase = Solution()
s = "anagram"
t = "nagaram"
print(testcase.isAnagram(s,t))