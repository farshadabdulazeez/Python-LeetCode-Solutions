# ** 1624. Largest Substring Between Two Equal Characters **

'''

Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

'''

# Solution

'''


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        last_index = {}
        max_length = -1
        
        for i, char in enumerate(s):
            max_length = max(max_length, i - last_index.setdefault(char, i) - 1)
            
        return max_length


'''



# Approach

'''

last_index = {}: Initializes an empty dictionary last_index to store the last index of each character.

max_length = -1: Initializes the maximum length variable to -1.

for i, char in enumerate(s):: Initiates a for loop that iterates through the characters of the input string s using enumerate to get both the index i and the character char.

max_length = max(max_length, i - last_index.setdefault(char, i) - 1): Updates max_length by taking the maximum of its current value and the calculated length of the substring between the current index i and the last index of the character. The setdefault method is used to get the last index from the dictionary, and if the character is not present, it sets the default value to the current index i.

return max_length: Returns the final maximum length of substrings between equal characters.

Time complexity:
 O(n)

Space complexity:
O(1)

'''

