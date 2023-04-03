'''283. Move Zeroes'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Goal :  Given an integer array nums, move all 0's to the end of it
                Keep order -> fast and slow pointer
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow],nums[fast] = nums[fast],nums[slow]  # a special swap method in Python
                slow += 1
        