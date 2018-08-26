"""
66. Plus One
DescriptionHintsSubmissionsDiscussSolution
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # we have to add one to the last item  anyway
        carry = 1
        
        for x in xrange(len(digits)-1, -1, -1):
            sum = digits[x] + carry
            if sum > 9: # or equal to 10
                digits[x] = sum %10
            else:
                digits[x] = sum
                carry = 0
                break
        if carry:
            digits[1:] = digits[0:]
            digits[0] = carry
        return digits
