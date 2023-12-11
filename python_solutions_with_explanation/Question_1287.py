# 1287. Element Appearing More Than 25% In Sorted Array


'''

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

'''

# Solution

'''


class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        threshold = len(arr) // 4

        for i in range(len(arr) - threshold):
            if arr[i] == arr[i + threshold]:
                return arr[i]

        return -1
        


'''

# Approach

'''

Calculate the threshold based on the length of the array.
Iterate through the array using a linear scan.
Check if the current element is equal to the element at an index threshold positions ahead. If true, return that element.

Time compplexity : 0(logn)

Space complexity : 0(1)

'''