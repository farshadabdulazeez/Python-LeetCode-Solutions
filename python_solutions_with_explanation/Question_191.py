# **191. Number of 1 Bits**
'''
Write a function that takes the binary representation of an unsigned integer and
returns the number of '1' bits it has (also known as the Hamming weight).
'''


# Solution :

'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

solution = Solution()
result = solution.hammingWeight(1234)
print(result)


'''


# Approach

'''
bin(n) converts the integer n to its binary representation as a string,
and then count('1') counts the number of set bits in that binary string.

Time complexity:
O(log n)

Space complexity:
0(1)

'''