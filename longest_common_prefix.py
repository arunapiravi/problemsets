Longest Common Prefix
  Go to Discuss
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ""
        
        if len(strs) == 1:
            return strs[0]    
        
        output = ""
        
        for index,char in enumerate(strs[0]):
            for other_string in strs[1:]:
                if index >= len(other_string) or other_string[index] != char:
                    return output
            output+=char
        return output
