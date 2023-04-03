'''367. Valid Perfect Square'''

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool

        Goal : Given a positive integer num, return true if num is a perfect square or false otherwise.
        """
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            mid_squre = mid ** 2
            if mid_squre > num:
                right = mid - 1
            elif mid_squre < num:
                left = mid + 1
            else:
                return True
        return False