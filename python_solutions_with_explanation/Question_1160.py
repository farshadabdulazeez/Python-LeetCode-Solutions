# 1160. Find Words That Can Be Formed by Characters

'''

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

'''

# Solution

'''


from collections import Counter

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        total_count = 0
        char_counts = Counter(chars)

        for word in words:
            word_counts = Counter(word)

            if all(word_counts[char] <= char_counts[char] for char in word):
                total_count += len(word)

        return total_count



'''

# Approach

'''

Counting Characters:

char_counts = Counter(chars): Count the occurrences of each character in the available characters using the Counter class.
Iterating through Words:

for word in words:: Iterate through each word in the list of words.
Checking if Word Can Be Formed:

word_counts = Counter(word): Count the occurrences of each character in the current word using Counter.
if all(word_counts[char] <= char_counts[char] for char in word):: Check if each character's count in the word is less than or equal to the count of the same character in the available characters. If true for all characters in the word, consider the word can be formed.
Updating Total Count:

total_count += len(word): If the word can be formed, add the length of the word to the total_count.
Returning Result:

return total_count: The final result is the total count of characters in words that can be formed.

Time complexity:
O(n + m), where n is the total number of characters in all words, and m is the length of the available characters string.

Space complexity:
O(m) due to the storage of character counts in the available characters.

'''