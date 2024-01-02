# ** 2553. Separate the Digits in an Array **

'''

Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.

To separate the digits of an integer is to get all the digits it has in the same order.

For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].

'''

# Solution

'''


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(digit) for num in nums for digit in str(num)]


'''



# Approach

'''

Iteration through nums:

for num in nums:: This loop iterates through each number in the input list.
Conversion of digits:

for digit in str(num): This nested loop converts each digit of the current number to an integer.
List comprehension:

[int(digit) for num in nums for digit in str(num)]: This constructs the final list containing all the separated digits.

Time complexity:
O(N * M), where N is the number of elements in nums, and M is the average number of digits in each number

The space complexity is O(N * M), as the new list generated contains all the separated digits from the input numbers.

'''

