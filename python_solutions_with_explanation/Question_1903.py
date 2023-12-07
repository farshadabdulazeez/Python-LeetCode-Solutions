# 1903. Largest Odd Number in String

'''
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.
'''

# Solution

''''


class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(len(num) - 1, -1, -1):
          if int(num[i]) % 2 != 0:
            return num[:i + 1]
        
        return ''


'''

# Approach

'''

Iterate from Right to Left:

Start iterating from the rightmost digit of the input string.
Find the rightmost odd digit.
Return Substring:

Return the substring of the original string starting from the beginning up to the rightmost odd digit found.
Handling No Odd Digits:

If no odd digits are found, return an empty string.

Time complexity : 0(n)

Space complexity : 0(1)

'''
