# 66. Plus One



'''

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

'''

# Solution

'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits 
        


'''

# Approach

'''

Iterate from Right to Left:

Start iterating from the rightmost digit of the digits list.
Check for 9:

If the current digit is 9, set it to 0.
Otherwise, increment the digit by 1 and return the modified list.
Add New Digit if Needed:

If the loop completes without returning, it means all digits were 9.
Add a new digit 1 to the left of the list.

Time complexity : 0(n)

Space complexity : 0(1)

'''