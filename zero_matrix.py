Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

# Space: O(m+n), runtime: O(mn)

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix[0]) # num of cols
        n = len(matrix) # number of rows
        
        row_zero = [0] * n
        col_zero = [0] * m
        
        for row in xrange(n):
            for col in xrange(m):
                if matrix[row][col] == 0:
                    row_zero[row] = 1
                    col_zero[col] = 1
        
        for row in xrange(n):
            for col in xrange(m):
                if row_zero[row] or col_zero[col]:
                    matrix[row][col] = 0
