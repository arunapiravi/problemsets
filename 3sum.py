#Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
#Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#Example:
#
#Given array nums = [-1, 2, 1, -4], and target = 1.
#
#The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Complexity = Medium

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_diff = 2**32
        closest = [0, 0, 0]
        for i in xrange(0, len(nums)-2):
            num1 = nums[i]
            for j in xrange(i+1, len(nums)-1):
                num2 = nums[j]
                num3 = target-(num1+num2)
                if num3 in nums[j+1:]:
                    closest = [num1, num2, num3]
                    return num1 + num2 + num3
                else:
                    for k in xrange(j+1, len(nums)):
                        third = nums[k]
                        diff = abs(num3 - third)
                        if diff < min_diff:
                            min_diff = diff
                            closest = [num1, num2, third]
                            sum = num1 + num2 + third
        return sum
