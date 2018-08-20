 Fair Candy Swap
DescriptionHintsSubmissionsDiscussSolution
Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

 

Example 1:

Input: A = [1,1], B = [2,2]
Output: [1,2]
Example 2:

Input: A = [1,2], B = [2,3]
Output: [1,2]
Example 3:

Input: A = [2], B = [1,3]
Output: [2,3]
Example 4:

Input: A = [1,2,5], B = [2,4]
Output: [5,4]
 

Note:

1 <= A.length <= 10000
1 <= B.length <= 10000
1 <= A[i] <= 100000
1 <= B[i] <= 100000
It is guaranteed that Alice and Bob have different total amounts of candy.
It is guaranteed there exists an answer.



### O(N^2) complexity

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ans = [0, 0]
        sum_a = sum(A)
        sum_b = sum(B)
        target = (sum_a + sum_b)/2
        
        
        for i in xrange(len(A)):
            for j in xrange(len(B)):
                if sum_a < target:
                    # swap smaller candy for bigger
                    if A[i] < B[j]:
                        if sum([B[j]] + A[:i] + A[i+1:]) == target:
                                ans = [A[i], B[j]]
                                break
                else:
                    # swap bigger for smaller
                    if A[i] > B[j]:
                        if sum([B[j]] + A[:i] + A[i+1:]) == target:
                                ans = [A[i], B[j]]  
                                break
        return ans


### O(N) complexity

/* We need to find a swap such that:
     * sum_of_candy_a - A[i] + B[j] == sum_of_candy_b - B[j] + A[i]
     * sum_of_candy_a - sum_of_candy_b == 2A[i] - 2B[j]
     * diff/2 = A[i] - B[j]
     *
     * for each A find in B if there is a  A[i] - diff/2
*/

def fairCandySwap(self, A, B):
        dif = (sum(A) - sum(B)) / 2
        A = set(A)
        for b in set(B):
            if dif + b in A:
                return [dif + b, b]

