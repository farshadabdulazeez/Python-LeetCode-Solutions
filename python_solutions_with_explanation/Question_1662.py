# 1662. Check If Two String Arrays are Equivalent

'''

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

'''

#Solution

'''


class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        str1 = ''.join(word1)
        str2 = ''.join(word2)

        return str1 == str2


'''

# Approach

'''

'join' method to concatenate all the strings in word1 and word2, respectively. This creates two new strings, str1 and str2, which represent the concatenation of all strings in the respective lists.
If they are equal, the method returns True, indicating that the concatenation of strings in word1 is equal to the concatenation of strings in word2. Otherwise, it returns False.

- Time complexity:
The join method has a time complexity of O(n), where n is the total length of the input list.

- Space complexity:
O(n)

'''
