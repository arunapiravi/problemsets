"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagrams = {}
        for string in strs:
            s = ''.join(sorted(string))
            if s in anagrams:
                anagrams[s].append(string)
            else:
                anagrams[s] = [string]
        return [anagrams[x] for x in anagrams]
