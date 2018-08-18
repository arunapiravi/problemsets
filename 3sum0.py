#Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

#Note:

#The solution set must not contain duplicate triplets.

#Example:

#Given array nums = [-1, 0, 1, 2, -1, -4],

#A solution set is:
#[
#  [-1, 0, 1],
#  [-1, -1, 2]
#]

#Complexity = Medium



class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for index1, i in enumerate(nums):
            for index2 in xrange(index1+1,len(nums)):
                j = nums[index2]
                k = -(i+j)
                if k > max(nums) or k < min(nums):
                    # the nullifier not present in nums
                    continue
                elif k in nums[index2+1:]:
                    sol = [i, j, k]
                    sol.sort()
                    if sol not in ans:
                        ans.append(sol)
        return ans
