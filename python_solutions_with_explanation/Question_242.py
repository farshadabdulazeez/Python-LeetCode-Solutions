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



The isAnagram function takes two string inputs, s and t, and returns a boolean indicating whether they are anagrams.

The function starts by checking if the lengths of strings s and t are equal. If they are not, the function immediately returns False because strings of different lengths cannot be anagrams.

Two dictionaries, count_s and count_t, are initialized to store the frequency counts of characters in strings s and t respectively.

The first for loop iterates through each character, i, in string s.
For each character, it updates the count in the count_s dictionary using the get method. If the character is not in the dictionary, it sets the count to 1; otherwise, it increments the existing count by 1.

The second for loop does the same for string t, updating the counts in the count_t dictionary.

Finally, the function returns True if the count_s dictionary is equal to the count_t dictionary, indicating that the two strings have the same character frequencies and are therefore anagrams. Otherwise, it returns False.

Time complexity : 0(n)

Space complexity : 0(1)

'''