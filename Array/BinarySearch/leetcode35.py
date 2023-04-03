'''35. Search Insert Position   O(log n) '''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int],  a sorted array of distinct integers 
        :type target: int
        :rtype: int

        Goal :  return the index if the target is found. If not, return the index where it would be if it were inserted in order.
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
        return right + 1 # insert position should have the number that greater than the target -> right
