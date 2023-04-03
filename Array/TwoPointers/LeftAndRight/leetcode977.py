'''977. Squares of a Sorted Array'''


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int] ->  non-decreasing order
        :rtype: List[int]

        Goal : return an array of the squares of each number sorted in non-decreasing order.
        """
        left, right = 0, len(nums) - 1
        ans = [[0] * len(nums)]
        while left <= right:
            l_sqr = nums[left] ** 2
            r_sqr = num[right] ** 2
            if l_Sqr < r_sqr:
                ans[]
