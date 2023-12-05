# 1688. Count of Matches in Tournament


'''

You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.

'''

# Solution

'''


class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        matches_played = 0
    
        while n > 1:
            matches_played += n // 2
            n = (n + 1) // 2
        
        return matches_played


'''

# Approach

'''

Initialize a variable matches_played to keep track of the total number of matches played in the tournament. Set it to 0 initially.
Start a while loop that continues as long as the number of teams n is greater than 1. The loop simulates the tournament rounds.
Inside the loop, increment matches_played by the number of matches played in the current round. If n is even, it adds n // 2 matches. Integer division (//) is used to get the floor division result.
Update the number of teams n for the next round. If n is even, it becomes n // 2. If n is odd, it becomes (n + 1) // 2, ensuring the correct number of teams advance to the next round.
 Once the loop exits (when there is only one team left), return the total number of matches played in the tournament.

Time complexity : O(log n) because in each iteration, the number of teams is reduced by half (or slightly more for odd numbers). The loop runs until there is only one team left.

Space complexity : 0(1)

'''