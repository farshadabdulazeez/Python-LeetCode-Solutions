# **1611. Minimum One Bit Operations to Make Integers Zero**

'''

Given an integer n, you must transform it into 0 using the following operations any number of times:

Change the rightmost (0th) bit in the binary representation of n.
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.

'''

#Solution

'''


class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        recursive_result = self.minimumOneBitOperations(n >> 1)
        result = n ^ recursive_result
        return result


'''

# Approach

''' 


if n == 0:: This line checks if the input n is 0.

return 0: If n is 0, the function returns 0, as there are no one-bit operations needed.

recursive_result = self.minimumOneBitOperations(n >> 1): This line is a recursive call to the minimumOneBitOperations method with n right-shifted by 1. It processes the next bit in the binary representation of n.

result = n ^ recursive_result: This line performs a bitwise XOR (^) operation between n and the result of the recursive call. This operation effectively flips the bits at corresponding positions where the recursive call flips bits.

return result: The final result is returned.


- Time complexity:
O(log n), where n is the input integer. Each recursive call processes one bit, and the recursion depth is logarithmic in the input size.

- Space complexity:
O(log n)


'''

