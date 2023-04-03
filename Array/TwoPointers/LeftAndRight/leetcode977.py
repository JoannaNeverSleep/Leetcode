'''977. Squares of a Sorted Array'''


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int] ->  non-decreasing order
        :rtype: List[int]

        Goal : return an array of the squares of each number sorted in non-decreasing order.
        """
        left, right = 0, len(nums) - 1
        ans = [0] * len(nums)
        k = len(nums) - 1
        while left <= right:
            l_sqr = nums[left] ** 2
            r_sqr = nums[right] ** 2
            if l_sqr < r_sqr:
                ans[k] = r_sqr
                right -= 1
            else:
                ans[k] = l_sqr
                left += 1
            k -= 1
        return ans
