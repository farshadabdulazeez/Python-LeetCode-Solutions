# 94. Binary Tree Inorder Traversal

'''

You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

'''

# Solution

'''


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        res = 0
        n = len(nums)
        
        for i in range(n):
            distinct = set()
            for j in range(i,n):
                distinct.add(nums[j])
                res += len(distinct) ** 2
                
        return res
        
        
'''

# Approach

'''


Initialize a variable res to 0 to store the final result.
Find the length of the input list nums and store it in the variable n.

Use two nested loops to iterate over all possible subarrays of nums.
The outer loop (i) represents the starting index of the subarray, ranging from 0 to n-1.
The inner loop (j) represents the ending index of the subarray, ranging from i to n-1.

Inside the inner loop, maintain a set called distinct to store unique elements within the current subarray.
For each element at index j, add it to the distinct set.

Calculate the square of the length of the distinct set and add it to the result (res) for each subarray.

Return the final result (res).

Time complexity : 0(n^2)

Space complexity : 0(n)


'''