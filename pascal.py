Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in xrange(1, numRows+1):
            triangle.append([1] * i)
            
        for i in xrange(2, numRows):
            row = triangle[i]
            for j in xrange(1, len(row)-1):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]        
        return triangle
