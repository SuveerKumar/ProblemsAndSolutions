""" 
Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 """

from math import *
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = x / abs(x)
        string_val = str(x)
        return_str = ""
        i = len(string_val) - 1
        while i > -1:
            return_str += string_val[i]
            i -= 1
        
        r_int = int(return_str)
        r_int *= sign
        if isinstance(r_int, int) == False:
            return 0
        
        return r_int

soln = Solution()
print soln.reverse(1534236469)
            
        
        