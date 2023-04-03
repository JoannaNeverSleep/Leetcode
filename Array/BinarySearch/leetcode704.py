''' 35. Binary Search   O(log n) '''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int], sorted in ascending order
        :type target: int
        :rtype: int

        Goal : write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1