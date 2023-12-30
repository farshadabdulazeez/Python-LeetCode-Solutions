# 414. Third Maximum Number


'''

Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

'''

# Solution

'''


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        if len(nums) > 2:
            return nums[-3]
        return nums[-1]
        
        
'''

# Approach

'''

The method aims to find and sum unique elements in the input list while ignoring duplicates.
It leverages a set to obtain unique elements and then uses a list comprehension to filter elements that occur only once in the original list.
The sum of these unique elements is calculated and returned.

Time complexity :  O(n^2)

Space complexity :  O(n)

'''