"""
A phrase is a palindrome if, after converting all uppercase
letters into lowercase letters and removing all non-alphanumeric
characters, it reads the same forward and backward. Alphanumeric
characters include letters and numbers.

Given a string s, return true if it is a palindrome,
or false other wise.
"""

class Solution():
    def isPalindrome(self, s):
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        print(s)
        for _ in range(len(s)):
            if s[_] != s[len(s)-_-1]:
                return False
        return True

testcase = Solution()
s = "A man, a plan, a canal: Panama"

print(testcase.isPalindrome(s))