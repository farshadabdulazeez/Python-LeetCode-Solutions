# ** 1. Two Sum **

'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

'''

# Solution

'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict:
                return [nums_dict[complement], i]
            nums_dict[num] = i


'''


# Approach

'''

The nums_dict dictionary is used to store the elements of nums and their corresponding indices.
The for loop iterates through each element in the nums list, and for each element, it calculates the complement (the value needed to reach the target).
If the complement is already in nums_dict, it means a pair of indices has been found, and the function returns those indices.
If not, the current element and its index are added to nums_dict.
The function returns the result as soon as a pair is found, making it an early exit algorithm.

Time complexity:
O(n)

Space complexity:
O(n)

'''
