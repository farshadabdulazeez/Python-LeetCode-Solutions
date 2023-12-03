# 1266. Minimum Time Visiting All Points

'''

On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

'''

# Solution

'''


class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        min_time = 0

        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            
            min_time += max(dx, dy)

        return min_time


'''

# Approach

'''

The minTimeToVisitAllPoints method in the Solution class iterates through the given list of points, calculating the absolute differences in x and y coordinates between consecutive points. For each pair of points, the maximum of these differences is added to the total minimum time, representing the time required to move from the previous point to the current one. The loop processes all points once, resulting in a linear time complexity of O(n), where n is the number of points.

- Time complexity:
The join method has a time complexity of O(n), where n is the total length of the input list.
O(n)

- Space complexity:
O(1)

'''