# 2544. Alternating Digit Sum


'''

You are given a positive integer n. Each digit of n has a sign according to the following rules:

The most significant digit is assigned a positive sign.
Each other digit has an opposite sign to its adjacent digits.
Return the sum of all digits with their corresponding sign.

'''

# Solution

'''


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum((-1) ** i * int(c) for i, c in enumerate(str(n)))
        
        
'''

# Approach

'''

Convert the input integer n to a string to easily iterate through its digits.
Use enumerate to get both the digit and its index in the string.
For each digit, calculate its contribution to the sum by multiplying it with the alternating sign (-1 or 1 based on the index).
Sum up all the contributions to get the alternating digit sum.

Time complexity :  O(d), where d is the number of digits in the integer n. The loop iterates through each digit once.

Space complexity :  O(1)

'''