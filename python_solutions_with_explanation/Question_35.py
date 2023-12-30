# 35. Search Insert Position


'''

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

'''

# Solution

'''


class Solution:
    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low
        
        


'''

# Approach

'''

Initialize Pointers:

low and high are initialized to the start and end of the array, respectively.
Binary Search:

Use a while loop to perform binary search until low is less than or equal to high.
Calculate the middle index (mid) of the current search range.
Check Middle Element:

If nums[mid] is equal to the target, return mid as the target is found.
If nums[mid] is less than the target, update low to mid + 1 to search in the right half.
If nums[mid] is greater than the target, update high to mid - 1 to search in the left half.
Return Position:

If the loop completes without finding the target, return low. This indicates the position where the target should be inserted.

Time complexity : 0(logn)

Space complexity : 0(1)

'''