'''26. Remove Duplicates from Sorted Array'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int] -> non-decreasing order,
        :rtype: int

        Goal : remove the duplicates in-place such that each unique element appears only once.  
                Then return the number of unique elements in nums.
                keep ordr -> fast and slow pointer
        """
        
        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast -1]:
                nums[slow] = nums[fast]
                slow += 1
        return slow

