
    
# 2108. Find First Palindromic String in the Array

'''

Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

'''

# Solution

''''


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]: return word
        return ""


'''

# Approach

'''

The function firstPalindrome takes a list of strings (words) as input.
It iterates through each word in the list using a for loop.
For each word, it checks if the word is a palindrome by comparing it to its reverse (word[::-1]).
If a palindrome is found, the function immediately returns that palindrome.
If no palindrome is found in the entire list, it returns an empty string.

Time complexity : 0(m+n)

Space complexity : 0(1)

'''
