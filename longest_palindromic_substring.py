#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

#Example 1:

#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

#Example 2:

#Input: "cbbd"
#Output: "bb"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        str = s
        if s == reversed(str):
            return s
        
        longest_pal = ""        
        for i in range(len(s)-len(longest_pal)):
            for j in range(len(s), i+len(longest_pal), -1):
                str = s[i:j]
                if str == str[::-1]:
                    if len(longest_pal) < len(str):
                        longest_pal = str
                        
        return longest_pal
