# 2264. Largest 3-Same-Digit Number in String

'''

You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.

'''

# Solution

'''


class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        max_good_integer = ""

        for i in range(len(num) - 2):
            current_substring = num[i:i+3]

            # Check if the substring is good (consists of only one unique digit)
            if len(set(current_substring)) == 1:
                current_digit = current_substring[0]

                # Update max_good_integer if the current one is greater
                if current_substring > max_good_integer:
                    max_good_integer = current_substring

        return max_good_integer


'''

# Approach

'''

Iterate Through Substrings:

Iterate through all possible 3-digit substrings of the given string num.
Check Good Substrings:

For each 3-digit substring, check if it is a good substring (consists of only one unique digit).
Update Maximum:

If a good substring is found, compare it with the current maximum good integer. If it is greater, update the maximum.
Return Result:

After iterating through all substrings, return the maximum good integer found.

Time Complexity: O(n)

Space Complexity: O(1)

'''