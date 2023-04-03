'''34. Find First and Last Position of Element in Sorted Array O(log n)'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int], sorted in non-decreasing order
        :type target: int
        :rtype: List[int]

        Goal : find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1].
        """
        def binarySearch(nums, target):
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
        
        index = binarySearch(nums, target)
        if index == -1:
            return [-1, -1]
        
        left, right = index, index
        while left - 1 >= 0 and nums[left -1] == target: left -= 1
        while right + 1 < len(nums) and nums[right + 1] == target: right += 1
        return [left, right]
