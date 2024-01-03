# ** 2540. Minimum Common Value **

'''

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

'''

# Solution

'''


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common_element = set(nums1).intersection(set(nums2))
        return min(common_element) if common_element else -1


'''


# Approach

'''

set(nums1) and set(nums2): Convert the input lists nums1 and nums2 into sets. A set is an unordered collection of unique elements.

set(nums1).intersection(set(nums2)): Find the intersection of the two sets. This operation returns a new set containing only the elements that are common to both set(nums1) and set(nums2).

n: Assign the result of the intersection to the variable n.

return min(n) if n else -1: If the set n is not empty (n is truthy), return the minimum element of the set using min(n). If the set is empty, return -1.

Time complexity:
O(min(m,n)),where m and n are the lengths of the input lists nums1 and nums2

Space complexity:
O(min(m,n))

'''
