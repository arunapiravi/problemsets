Count and Say
  Go to Discuss
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return None
        
        pre_n = [1]
        
        if n == 1:
            return str(pre_n[0])
        
        n_term = []
        count = 1
        n_counter = 2
        
        while n_counter <= n:
            for i in xrange(0, len(pre_n)):
                if i+1 == len(pre_n):
                    n_term.append(count)
                    n_term.append(pre_n[i])
                    n_counter += 1
                    break
                if pre_n[i+1] == pre_n[i]:
                    count += 1
                else:
                    n_term.append(count)
                    n_term.append(pre_n[i])
                    count = 1
            pre_n = n_term
            n_term = []
            count = 1
        
        n_term = ""
        for num in pre_n:
            n_term += str(num) 
        return n_term 
