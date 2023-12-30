# 242.Valid Anagram

'''

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

'''

# Solution

'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        
        count_s = {}
        count_t = {}

        for i in  s:
            count_s[i] = count_s.get(i, 0) + 1
        for j in t:
            count_t[j] = count_t.get(j, 0) + 1
        
        return count_s == count_t
        
        


'''

# Approach

'''

The function starts by checking if the lengths of strings s and t are equal. If they are not, the function immediately returns False because strings of different lengths cannot be anagrams.
The code then uses a list comprehension to compare corresponding characters in the two strings.
zip(s, t) creates pairs of corresponding characters from strings s and t.
all(i == j for i, j in zip(s, t)) checks if all pairs have equal characters.
The all function returns True if all elements of the iterable are true, and False otherwise.

Time complexity : 0(n)

Space complexity : 0(1)

'''