'''69. Sqrt(x)'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

        Goal : return the square root of x rounded down to the nearest integer.  0 <= x <= 2^{31} - 1
        """
        left, right = 0, 2**16
        while left <= right:
            mid = left + (right - left) // 2
            mid_squre = mid**2
            if mid_squre > x:
                right = mid - 1
            elif mid_squre < x:
                left = mid + 1
            else:
                return mid
        return right