Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

complexity: Medium, runtime :O(N!), space: O(N)

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return [nums]
        
        ans = []
        for index in xrange(len(nums)):
            num = nums[index]
            rest = nums[:index] + nums[index+1:]
            for perm in self.permute(rest):
                if type(perm) == list:
                    ans.append([num] + perm)
                else:
                    ans.append([num] + [perm])
        return ans


