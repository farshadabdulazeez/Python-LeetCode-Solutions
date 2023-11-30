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
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


'''



# Approach

'''

The approach used here is a nested loop. The outer loop iterates through each element in the nums list, and the inner loop iterates through the elements that come after the current element in the outer loop. For each pair of indices (i, j), the function checks if the corresponding elements in the array add up to the target.

If a pair is found, the function immediately returns the indices as a list [i, j]. This approach assumes that there is exactly one solution, and it doesn't handle cases where there might be multiple valid pairs..

Time complexity:
 O(n^2)

Space complexity:
O(1)

'''

